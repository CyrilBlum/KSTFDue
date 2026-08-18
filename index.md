---
layout: default
title: ⭐ Startseite
nav_order: 1
---

# Software-Installation KST FDü

Diese Seite enthält Installationsanleitungen für alle an der Kantonsschule Dübendorf (KST FDü) verwendeten Programme, geordnet nach Fachschaft.

Wo immer möglich werden Anleitungen für **Windows** (mit winget) und **macOS** (mit Homebrew) bereitgestellt. Befehle können direkt aus den Codeblöcken kopiert werden.

## Hinweise

- **Windows:** Befehle müssen in **PowerShell als Administrator** ausgeführt werden. Falls `winget` den Zertifikatsfehler *„The server certificate did not match any of the expected values“* anzeigt, vorher `winget settings --enable BypassCertificatePinningForMicrosoftStore` ausführen:
![PowerShell unter Windows als Administrator](docs/assets/images/PowerShell.png)
- **macOS:** ⚠️ **Wichtig:** Die Anleitungen funktionieren nur mit installiertem Homebrew. Falls Homebrew noch nicht installiert ist, zuerst die Seite [Homebrew einrichten](docs/homebrew.html) befolgen. Befehle müssen in der **Terminal-App** ausgeführt werden. Öffnen Sie ein **Terminal**, indem Sie die Spotlight-Suche mit Cmd + Leertaste öffnen, Terminal eingeben und mit Enter bestätigen.
![Terminal unter macOS öffnen](docs/assets/images/Terminal.png)

## Kurzzeitgymnasium (KG)
Schnelle Installation und Verwaltung für das Kurzzeitgymnasium:

- [⭐️ Schnellinstallation (Windows & macOS)](docs/kg/schnellinstallation.html)
- [⭐️ Installationscheck (Windows & macOS)](docs/kg/verifikation.html)
- [Fachschaften](docs/kg/fachschaften.html) – Programme nach Fachschaft

## Handelsmittelschule (HMS)
Schnelle Installation und Verwaltung für die Handelsmittelschule:

- [⭐️ Schnellinstallation (Windows & macOS)](docs/hms/schnellinstallation.html)
- [⭐️ Installationscheck (Windows & macOS)](docs/hms/verifikation.html)

## Weitere Tools
- [⭐️ Deinstallation (Windows & macOS)](docs/deinstallation.html) – Tools entfernen
- [macOS: Homebrew einrichten](docs/homebrew.html)
