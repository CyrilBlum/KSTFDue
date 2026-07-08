---
layout: default
title: iCal zu HTML
nav_exclude: true
search_exclude: true
---

# iCal zu HTML

<div class="ical-tool">
  <div class="ical-field">
    <label for="ical-url">iCal-URL</label>
    <input id="ical-url" type="text" inputmode="url" value="https://intranet.tam.ch/klw/rest/ics/type/calendar/date/1783439452/auth/gr001@Y3lyaWwuYmx1bQ==:Y2JhMDMyNTkyNmI1NmFiNjAxZTBhN2JmNzA4N2M1ZDNmOWQyMTUwMw==/calendar.ics">
  </div>

  <p class="ical-hint">
    Die URL wird direkt an Python weitergegeben.
  </p>

  <fieldset>
    <legend>Ausgabe</legend>
    <label>
      <input type="radio" name="event-mode" value="next" checked>
      Nächste Termine
    </label>
    <label>
      <input type="radio" name="event-mode" value="all">
      Alle Termine
    </label>
    <label class="inline-number">
      Anzahl
      <input id="event-limit" type="number" min="1" step="1" value="3">
    </label>
  </fieldset>

  <div class="ical-actions">
    <button id="generate-html" type="button">HTML generieren</button>
    <button id="copy-html" type="button" disabled>HTML kopieren</button>
  </div>

  <p id="ical-status" role="status">Bereit.</p>
  <textarea id="html-output" rows="18" spellcheck="false" readonly></textarea>
</div>

<style>
  .ical-tool {
    display: grid;
    gap: 1rem;
    max-width: 58rem;
  }

  .ical-field,
  .ical-actions,
  .inline-number {
    display: flex;
    gap: .6rem;
    align-items: center;
  }

  .ical-field {
    flex-wrap: wrap;
  }

  .ical-field label,
  .inline-number {
    font-weight: 600;
  }

  #ical-url {
    flex: 1 1 24rem;
    min-width: 16rem;
  }

  #ical-url,
  .ical-tool input[type="number"],
  .ical-tool textarea {
    border: 1px solid #bbb;
    border-radius: 4px;
    padding: .45rem .55rem;
    font: inherit;
  }

  .ical-tool input[type="number"] {
    width: 5rem;
  }

  .ical-tool fieldset {
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: .8rem 1rem;
  }

  .ical-tool fieldset label {
    margin-right: 1rem;
  }

  .ical-actions {
    flex-wrap: wrap;
  }

  .ical-actions button {
    border: 1px solid #555;
    border-radius: 4px;
    padding: .45rem .8rem;
    background: #fff;
    color: #222;
    cursor: pointer;
  }

  .ical-actions button:disabled {
    border-color: #bbb;
    color: #777;
    cursor: not-allowed;
  }

  #ical-status {
    margin: 0;
  }

  .ical-hint {
    margin: 0;
    color: #555;
  }

  #html-output {
    width: 100%;
    min-height: 24rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: .85rem;
  }
</style>

<script>
  const helperEndpoint = (() => {
    if (location.hostname === "127.0.0.1" || location.hostname === "localhost") {
      return "http://127.0.0.1:8765/convert";
    }
    return new URL("{{ site.baseurl }}/ical-to-html/convert", location.origin).href;
  })();
  const statusEl = document.querySelector("#ical-status");
  const outputEl = document.querySelector("#html-output");
  const urlInput = document.querySelector("#ical-url");
  const copyButton = document.querySelector("#copy-html");
  const generateButton = document.querySelector("#generate-html");
  const limitInput = document.querySelector("#event-limit");
  const modeInputs = document.querySelectorAll("input[name='event-mode']");

  function setStatus(message) {
    statusEl.textContent = message;
  }

  function selectedLimit() {
    const mode = document.querySelector("input[name='event-mode']:checked").value;
    if (mode === "all") {
      return null;
    }
    return Math.max(1, Number.parseInt(limitInput.value || "3", 10));
  }

  function getIcalUrl() {
    const url = urlInput.value.trim();
    if (!url) {
      throw new Error("Bitte eine iCal-URL eingeben.");
    }
    if (!/^https?:\/\//i.test(url)) {
      throw new Error("Bitte eine gültige iCal-URL mit http:// oder https:// eingeben.");
    }
    return url;
  }

  async function generateHtml() {
    try {
      generateButton.disabled = true;
      copyButton.disabled = true;
      outputEl.value = "";
      setStatus("URL wird an Python übergeben...");

      const url = getIcalUrl();
      const limit = selectedLimit();
      let response;
      try {
        response = await fetch(helperEndpoint, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ url, limit }),
        });
      } catch (error) {
        throw new Error(`Python-Webserver nicht erreichbar: ${helperEndpoint}`);
      }

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Python konnte das HTML nicht generieren.");
      }

      outputEl.value = data.html;
      copyButton.disabled = false;
      setStatus("HTML generiert.");
    } catch (error) {
      setStatus(error.message);
    } finally {
      generateButton.disabled = false;
    }
  }

  async function copyHtml() {
    await navigator.clipboard.writeText(outputEl.value);
    setStatus("HTML in die Zwischenablage kopiert.");
  }

  modeInputs.forEach((input) => {
    input.addEventListener("change", () => {
      limitInput.disabled = document.querySelector("input[name='event-mode']:checked").value === "all";
    });
  });

  generateButton.addEventListener("click", generateHtml);
  copyButton.addEventListener("click", copyHtml);
</script>
