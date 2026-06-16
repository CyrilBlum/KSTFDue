---
layout: default
title: Informatik
parent: Fachschaften
nav_order: 4
---

# Informatik

Programme für den Informatikunterricht. Alle Programme werden im Rahmen des BYOD-Konzepts auf dem persönlichen Gerät der Schülerinnen installiert.

## Ansprechpersonen

| Programm | Ansprechperson |
|---|---|
| VS Code, Python, Filius | Cyril Blum |

---

## VS Code

Visual Studio Code (VS Code) ist die Entwicklungsumgebung für den Informatikunterricht.

### Windows

```powershell
winget install -e --id Microsoft.VisualStudioCode --scope machine --silent --accept-package-agreements --accept-source-agreements --silent
```

### macOS

```bash
brew install --cask visual-studio-code
```

---

## Python und pip

Python ist die Programmiersprache des Informatikunterrichts. `pip` (Paketmanager für Python) wird automatisch mitinstalliert.

### Windows

```powershell
winget install -e --id Python.Python.3.13 --scope machine --silent --accept-package-agreements --accept-source-agreements --silent
```

### macOS

```bash
brew install python3
```

---

## Filius

Filius ist eine Netzwerksimulationssoftware für den Unterricht. Sie ermöglicht das Erstellen und Testen von Netzwerken.

### Windows

```powershell
winget install -e --id StefanFreischlad.Filius --scope machine --silent --accept-package-agreements --accept-source-agreements --silent
```

### macOS

Filius ist nicht über Homebrew verfügbar. Download unter:

[lernsoftware-filius.de](https://www.lernsoftware-filius.de)

Die macOS-Version herunterladen und installieren.
