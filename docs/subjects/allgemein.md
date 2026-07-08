---
layout: default
title: Alle Fächer
parent: Fachschaften
nav_order: 1
---

# Alle Fächer

Diese Programme werden in allen Fächern benötigt und müssen von allen Schülerinnen installiert werden.

## Ansprechpersonen

| Programm | Ansprechperson |
|---|---|
| SafeExamBrowser | Cyril Blum (IT) |
| Microsoft 365 | IT |

---

## SafeExamBrowser

SafeExamBrowser ist ein gesicherter Prüfungsbrowser, der während digitalen Prüfungen den Zugriff auf das Internet und andere Programme sperrt.


### Windows

```powershell
winget install -e --id ETHZurich.SafeExamBrowser --scope machine --silent --accept-package-agreements --accept-source-agreements --silent
```

### macOS

```bash
brew install --cask safe-exam-browser
```

---

## Microsoft 365

Microsoft 365 (Word, Excel, PowerPoint, Teams usw.) steht als Webanwendung unter [office.com](https://www.office.com) zur Verfügung und kann zusätzlich lokal installiert werden.

- **Webzugang:** [office.com](https://www.office.com) – Login mit der schulischen E-Mail-Adresse

### Windows

Microsoft 365 sollte unter Windows bereits vorinstalliert sein. Starten Sie eine beliebige Anwendung aus dem Microsoft-365-Paket (z. B. Word). Danach müssen Sie sich mit der schulischen E-Mail-Adresse anmelden, um die Lizenz zu aktivieren.

### macOS

```bash
brew install --cask microsoft-office
```

Danach müssen Sie sich mit der schulischen E-Mail-Adresse anmelden, um die Lizenz zu aktivieren.

---

## Rectangle (nur macOS)
Rectangle ist ein Fenster-Manager für macOS, der die Anordnung von Fenstern erleichtert.

### macOS

```bash
brew install --cask rectangle
```