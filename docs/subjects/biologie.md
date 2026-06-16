---
layout: default
title: Biologie
parent: Fachschaften
nav_order: 3
---

# Biologie

Programme für den Biologieunterricht. Die meisten Programme werden im Rahmen des BYOD-Konzepts auf dem persönlichen Gerät der Schülerinnen installiert.

## Ansprechpersonen

| Programm | Ansprechperson |
|---|---|
| ApE, ImageJ / Fiji, CellProfiler, MEGA, GraphPad Prism, Plickers, Brian | Nadine Ahorn, Benjamin Volkmer |

---

## ApE – A Plasmid Editor

ApE ist ein kostenloser Plasmid-Editor für die Molekularbiologie.

### Windows

ApE ist nicht über winget verfügbar. Download unter: [jorgensen.biology.utah.edu/wayned/ape](http://jorgensen.biology.utah.edu/wayned/ape/). Nach dem Download: Das heruntergeladene `zip`-Archiv entpacken, den Ordner in `ApE` umbenennen und diesen, sowie dessen Inhalt, in `C:\Program Files\ApE` verschieben.

### macOS

```bash
brew install --cask ape
```

---

## ImageJ / Fiji

ImageJ (bzw. die erweiterte Distribution Fiji) ist ein Programm für die (semi-automatische) Bildanalyse.

### Windows

Fiji (ImageJ) ist nicht über winget verfügbar. Download unter: [fiji.sc](https://fiji.sc). Nach dem Download: Die heruntergeladene `zip`-Datei entpacken, den Ordner in `Fiji` umbenennen und diesen, sowie dessen Inhalt, in `C:\Program Files\Fiji` verschieben.

### macOS

```bash
brew install --cask fiji
```

---

## CellProfiler

CellProfiler ist eine Software für die automatische Bildanalyse von Zellen.

### Windows

CellProfiler ist nicht über winget verfügbar. Download unter: [cellprofiler.org](https://cellprofiler.org). Die Windows-Version herunterladen, das `exe`-File anklicken und das Programm installieren.

### macOS

```bash
brew install --cask cellprofiler
```

---

## MEGA

MEGA (Molecular Evolutionary Genetics Analysis) wird für Alignments und phylogenetische Bäume verwendet.

### Windows

```powershell
winget install -e --id iGEM.MEGA.12 --scope machine --silent --accept-package-agreements --accept-source-agreements --silent
```

### macOS

```bash
brew install --cask mega
```

---

## GraphPad Prism

GraphPad Prism ist ein kostenpflichtiges Programm zur Erstellung wissenschaftlicher Grafiken und Statistiken.

### Windows

```powershell
winget install -e --id GraphPad.Prism --scope machine --silent --accept-package-agreements --accept-source-agreements --silent
```

Die Aktivierung des Programms erfolgt über eine institutionelle Lizenz. Für den Zugang an die Ansprechpersonen wenden.

### macOS

```bash
brew install --cask prism
```

Download unter: [graphpad.com](https://www.graphpad.com)