---
layout: default
title: WinGet Problemlösung
nav_order: 5
---

# WinGet Problemlösung (Windows)

`winget` (Windows Package Manager) ist das offizielle Microsoft-Tool zum automatischen Installieren und Aktualisieren von Software unter Windows 10 und 11.

Falls bei der Schnellinstallation oder der Installation einzelner Pakete über `winget` Fehler auftreten, finden Sie hier die häufigsten Ursachen und Lösungen.

---

## 1. Zertifikatsfehler (`The server certificate did not match any of the expected values`)

**Symptom:**  
Die Installation bricht ab mit der Fehlermeldung *„The server certificate did not match any of the expected values“* oder allgemein mit Zertifikatsfehlern beim Verbinden mit dem Microsoft Store / WinGet-CDN.

**Ursache:**  
Dies geschieht häufig in Schul- oder Unternehmensnetzwerken mit SSL-Inspektion / Proxies, wenn Windows-Store-Zertifikate veraltet sind oder vom Netzwerk anders aufgelöst werden (Certificate Pinning).

**Lösung:**  
Öffnen Sie **PowerShell als Administrator** (*Windows-Taste → „PowerShell“ → Rechtsklick → „Als Administrator ausführen“*) und führen Sie folgenden Befehl aus:

```powershell
winget settings --enable BypassCertificatePinningForMicrosoftStore
```

Führen Sie den Installationsbefehl danach erneut aus.

---

## 2. Fehler `403 Forbidden` / *„Nicht zulässig“* (insb. bei GraphPad Prism)

**Symptom:**  
Beim Herunterladen von Paketen (häufig bei `GraphPad.Prism`) erscheint die Fehlermeldung `HTTP 403: Forbidden` oder *„Zugriff nicht zulässig“*.

**Ursache:**  
Server von Herstellern (oder deren CDNs wie Cloudflare) blockieren automatische Downloads von `winget`-Anfragen, wenn diese über Schul-IP-Adressen oder ohne Browser-User-Agent gesendet werden (DDoS-Schutz / IP-Rate-Limiting). Zudem können Schul-Firewalls direkte EXE-Downloads unterbinden.

**Lösung:**  
- **Option A (Empfohlen): Manueller Browser-Download**  
  Da normale Webbrowser durchgelassen werden, laden Sie das Programm direkt über die Website herunter (z. B. für GraphPad unter [graphpad.com/updates](https://www.graphpad.com/updates)) und führen Sie die `.exe`-Datei aus.
- **Option B: Netzwerk wechseln**  
  Verbinden Sie Ihr Gerät kurzzeitig mit einem anderen Netzwerk (z. B. mobiler Hotspot über das Smartphone), um den Download über `winget` erneut zu versuchen.

---

## 3. Suche oder Installation schlägt fehl (`0x8a15000f` / Paketquelle beschädigt)

**Symptom:**  
Befehle wie `winget install` oder `winget search` scheitern mit dem Fehlercode `0x8a15000f` oder dem Hinweis *„Paketquelle konnte nicht gelesen werden“*.

**Ursache:**  
Die lokale WinGet- / App-Installer-Installation bzw. die Registrierung der Paketquellen auf dem Computer ist beschädigt.

**Lösung (Reparatur via PowerShell):**  
Microsoft empfiehlt für solche Fälle explizit das PowerShell-Modul `Repair-WinGetPackageManager`.

1. Öffnen Sie **PowerShell als Administrator** (*Windows-Taste → „PowerShell“ → Rechtsklick → „Als Administrator ausführen“*).
2. Führen Sie nacheinander folgende Befehle aus:

```powershell
Install-PackageProvider -Name NuGet -Force
Install-Module -Name Microsoft.WinGet.Client -Force -Repository PSGallery
```

> **Hinweis:** Falls PowerShell nach einem „nicht vertrauenswürdigen Repository“ fragt, bestätigen Sie mit **J** (Ja) bzw. **Y** (Yes).

3. Führen Sie anschliessend den Reparatur-Befehl aus:

```powershell
Repair-WinGetPackageManager -Force -Latest
```

Nach Abschluss des Reparaturvorgangs PowerShell neu starten und die Installation erneut versuchen.
