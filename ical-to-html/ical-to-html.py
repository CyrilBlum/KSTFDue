#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import html
import json
from collections import defaultdict
from datetime import date, datetime, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
from urllib.request import urlopen

try:
    from icalendar import Calendar
except ImportError:
    Calendar = None


ICAL_URL = "https://intranet.tam.ch/klw/rest/ics/type/calendar/date/1783439452/auth/gr001@Y3lyaWwuYmx1bQ==:Y2JhMDMyNTkyNmI1NmFiNjAxZTBhN2JmNzA4N2M1ZDNmOWQyMTUwMw==/calendar.ics"
CONVERT_PATHS = {
    "/convert",
    "/ical-to-html/convert",
    "/KSTFDue/ical-to-html/convert",
}

MONTHS_DE = {
    "January": "Januar", "February": "Februar", "March": "März", "April": "April",
    "May": "Mai", "June": "Juni", "July": "Juli", "August": "August",
    "September": "September", "October": "Oktober", "November": "November", "December": "Dezember",
}

DAYS_DE = {
    "Monday": "Montag", "Tuesday": "Dienstag", "Wednesday": "Mittwoch",
    "Thursday": "Donnerstag", "Friday": "Freitag", "Saturday": "Samstag", "Sunday": "Sonntag",
}


def looks_like_url(value):
    return value.strip().lower().startswith(("http://", "https://"))


def validate_url(url):
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Bitte eine gültige iCal-URL mit http:// oder https:// eingeben.")


def normalize_dt(value):
    if isinstance(value, datetime):
        if value.tzinfo is not None:
            return value.replace(tzinfo=None)
        return value
    if isinstance(value, date):
        return datetime.combine(value, time.min)
    return datetime.min


def unfold_ical_lines(ical_content):
    if isinstance(ical_content, bytes):
        ical_content = ical_content.decode("utf-8", errors="replace")

    lines = []
    for raw_line in ical_content.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if raw_line.startswith((" ", "\t")) and lines:
            lines[-1] += raw_line[1:]
        else:
            lines.append(raw_line)
    return lines


def unescape_ical_text(value):
    return (
        value
        .replace("\\n", "\n")
        .replace("\\N", "\n")
        .replace("\\,", ",")
        .replace("\\;", ";")
        .replace("\\\\", "\\")
    )


def parse_ical_datetime(value):
    value = value.strip()
    if not value:
        return None

    if value.endswith("Z"):
        value = value[:-1]

    for fmt in ("%Y%m%dT%H%M%S", "%Y%m%dT%H%M", "%Y%m%d"):
        try:
            parsed = datetime.strptime(value, fmt)
        except ValueError:
            continue

        if fmt == "%Y%m%d":
            return parsed.date()
        return parsed

    return None


def parse_events_basic(ical_content):
    events = []
    current_event = None

    for line in unfold_ical_lines(ical_content):
        if line == "BEGIN:VEVENT":
            current_event = {}
            continue
        if line == "END:VEVENT":
            if current_event is not None:
                events.append({
                    "summary": current_event.get("SUMMARY", "Ohne Titel"),
                    "start": parse_ical_datetime(current_event.get("DTSTART", "")),
                    "description": current_event.get("DESCRIPTION", ""),
                })
            current_event = None
            continue
        if current_event is None or ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.split(";", 1)[0].upper()
        if key in {"SUMMARY", "DESCRIPTION"}:
            current_event[key] = unescape_ical_text(value)
        elif key == "DTSTART":
            current_event[key] = value

    events.sort(key=lambda event: normalize_dt(event["start"]))
    return events


def parse_events(ical_content):
    if Calendar is None:
        return parse_events_basic(ical_content)

    cal = Calendar.from_ical(ical_content)
    events = []

    for component in cal.walk():
        if component.name != "VEVENT":
            continue

        start = component.get("dtstart")
        start_dt = start.dt if start else None
        events.append({
            "summary": str(component.get("summary", "Ohne Titel")),
            "start": start_dt,
            "description": str(component.get("description", "")),
        })

    events.sort(key=lambda event: normalize_dt(event["start"]))
    return events


def is_future_event(event, now=None):
    now = now or datetime.now()
    start = event["start"]

    if isinstance(start, datetime):
        return normalize_dt(start) >= now
    if isinstance(start, date):
        return start >= now.date()
    return False


def event_month(event):
    start = event["start"]
    if not start:
        return "00-0000", "Ohne Datum"

    month_en = start.strftime("%B")
    month_de = MONTHS_DE.get(month_en, month_en)
    return start.strftime("%m-%Y"), f"{month_de} {start.strftime('%Y')}"


def event_display_values(event):
    start = event["start"]
    if not start:
        return "Kein Datum", ""

    date_str = start.strftime("%d.%m.%Y")
    day_de = DAYS_DE.get(start.strftime("%A"), start.strftime("%A"))

    if isinstance(start, datetime):
        return date_str, f"{day_de}, {start.strftime('%H:%M')}"

    return date_str, day_de


def event_description(event):
    description = event["summary"]
    if event["description"]:
        description += f" - {event['description']}"
    return description


def select_events(events, limit=None, now=None):
    if limit is None:
        return events
    return [event for event in events if is_future_event(event, now)][:limit]


def generate_calendar_html(ical_content, limit=None, title="Kalender", subscribe_url=ICAL_URL, now=None):
    events = select_events(parse_events(ical_content), limit, now)
    grouped_events = defaultdict(list)
    month_headers = {}

    for event in events:
        month_key, month_header = event_month(event)
        grouped_events[month_key].append(event)
        month_headers[month_key] = month_header

    escaped_title = html.escape(title)
    escaped_url = html.escape(subscribe_url, quote=True)

    lines = [
        "<!DOCTYPE html>",
        '<html lang="de">',
        "<head>",
        '  <meta charset="UTF-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f"  <title>{escaped_title}</title>",
        "  <style>",
        "    body { font-family: Arial, sans-serif; margin: 2rem; color: #222; line-height: 1.5; }",
        "    h1 { font-size: 1.75rem; margin: 0 0 1rem; }",
        "    h2 { font-size: 1.1rem; margin: 1.75rem 0 .5rem; border-bottom: 1px solid #bbb; padding-bottom: .25rem; }",
        "    table { width: 100%; border-collapse: collapse; }",
        "    td { padding: .5rem .25rem; border-bottom: 1px solid #e5e5e5; vertical-align: top; }",
        "    td:first-child { width: 7rem; font-weight: 700; }",
        "    td:nth-child(2) { width: 10rem; color: #555; }",
        "    .subscribe { margin-bottom: 1.5rem; }",
        "  </style>",
        "</head>",
        "<body>",
        f"<h1>{escaped_title}</h1>",
        f'<p class="subscribe"><a href="{escaped_url}">Kalender abonnieren</a></p>',
    ]

    for month_key, month_events in grouped_events.items():
        lines.append(f"<h2>{html.escape(month_headers[month_key])}</h2>")
        lines.append("<table>")

        for event in month_events:
            date_str, time_display = event_display_values(event)
            lines.append(
                "<tr>"
                f"<td>{html.escape(date_str)}</td>"
                f"<td>{html.escape(time_display)}</td>"
                f"<td>{html.escape(event_description(event))}</td>"
                "</tr>"
            )

        lines.append("</table>")

    if not events:
        lines.append("<p>Keine passenden Termine gefunden.</p>")

    lines.extend(["</body>", "</html>"])
    return "\n".join(lines)


def fetch_ical(url):
    validate_url(url)
    with urlopen(url, timeout=20) as response:
        return response.read()


def generate_calendar_html_from_url(url, limit=None, title="Kalender"):
    ical_content = fetch_ical(url)
    return generate_calendar_html(
        ical_content,
        limit=limit,
        title=title,
        subscribe_url=url,
    )


class CalendarRequestHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        if self.path not in {"/", "/health"}:
            self.send_error(404)
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True}).encode("utf-8"))

    def do_POST(self):
        if self.path not in CONVERT_PATHS:
            self.send_error(404)
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(content_length).decode("utf-8"))
            url = payload["url"]
            limit = payload.get("limit")
            if limit is not None:
                limit = int(limit)
            generated_html = generate_calendar_html_from_url(url, limit=limit)
            response = {"html": generated_html}
            status = 200
        except Exception as exc:
            response = {"error": str(exc)}
            status = 500

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


def serve(host="127.0.0.1", port=8765):
    server = ThreadingHTTPServer((host, port), CalendarRequestHandler)
    print(f"iCal-zu-HTML-Helper läuft auf http://{host}:{port}")
    print("Mit Ctrl+C beenden.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nHelper beendet.")
    finally:
        server.server_close()


def generate_calendar_html_from_source(source, source_kind="auto", limit=None, title="Kalender", subscribe_url=ICAL_URL, now=None):
    if source_kind == "auto":
        source_kind = "url" if looks_like_url(source) else "content"

    if source_kind == "url":
        ical_content = fetch_ical(source)
        subscribe_url = source
    else:
        ical_content = source

    return generate_calendar_html(
        ical_content,
        limit=limit,
        title=title,
        subscribe_url=subscribe_url,
        now=now,
    )


def main():
    parser = argparse.ArgumentParser(description="Erstellt eine HTML-Kalenderseite aus einer iCal-Datei.")
    parser.add_argument("--url", default=ICAL_URL, help="URL der iCal-Datei")
    parser.add_argument("--output", default="kalender.html", help="Pfad der HTML-Ausgabedatei")
    parser.add_argument("--limit", type=int, help="Nur die nächsten N Termine ausgeben")
    parser.add_argument("--serve", action="store_true", help="Lokalen Helper-Server für die Jekyll-Seite starten")
    parser.add_argument("--host", default="127.0.0.1", help="Host für --serve")
    parser.add_argument("--port", type=int, default=8765, help="Port für --serve")
    args = parser.parse_args()

    if args.serve:
        serve(args.host, args.port)
        return

    ical_content = fetch_ical(args.url)
    generated_html = generate_calendar_html(ical_content, limit=args.limit, subscribe_url=args.url)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(generated_html)

    event_count = len(select_events(parse_events(ical_content), args.limit))
    print(f"HTML-Datei erstellt: {args.output}")
    print(f"{event_count} Events verarbeitet")


if __name__ == "__main__":
    main()
