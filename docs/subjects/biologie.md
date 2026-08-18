---
layout: default
title: Biologie
parent: Fachschaften
nav_order: 3
---

# Biologie

Programme für den Biologieunterricht. Die meisten Programme werden im Rahmen des BYOD-Konzepts auf dem persönlichen Gerät der Schülerinnen installiert.

## Ansprechpersonen & Bildungsgänge

| Programm | Zielgruppe | Ansprechperson |
|---|---|---|
| MEGA | KG & HMS | Nadine Ahorn, Benjamin Volkmer |
| GraphPad Prism | KG & HMS | Nadine Ahorn, Benjamin Volkmer |
| ApE | Nur KG | Nadine Ahorn, Benjamin Volkmer |
| ImageJ / Fiji | Nur KG | Nadine Ahorn, Benjamin Volkmer |
| CellProfiler | Nur KG | Nadine Ahorn, Benjamin Volkmer |
| Plickers, Brian | Lehrpersonen | Nadine Ahorn, Benjamin Volkmer |

---

## ApE – A Plasmid Editor

ApE ist ein kostenloser Plasmid-Editor für die Molekularbiologie.

### Windows

ApE ist nicht über winget verfügbar. Download unter: [jorgensen.biology.utah.edu/wayned/ape](http://jorgensen.biology.utah.edu/wayned/ape/).

**Anleitung für Windows 10 (ZIP entpacken und verschieben):**
1. **Herunterladen:** Laden Sie das ZIP-Archiv herunter (liegt anschliessend im Ordner *Downloads*).
2. **Entpacken:** Öffnen Sie den Ordner *Downloads*, machen Sie einen **Rechtsklick** auf die ZIP-Datei und wählen Sie **„Alle extrahieren…“**. Klicken Sie im Fenster unten rechts auf **„Extrahieren“**.
3. **Ordner umbenennen:** Machen Sie einen Rechtsklick auf den neu entstandenen (entpackten) Ordner, wählen Sie **„Umbenennen“** und nennen Sie den Ordner exakt `ApE`.
4. **Nach `C:\Program Files` verschieben:**
   - Schneiden Sie den Ordner `ApE` aus (Rechtsklick → **„Ausschneiden“** oder Tastenkombination `Strg + X`).
   - Öffnen Sie im Windows Explorer: **Dieser PC → Lokaler Datenträger (C:) → Program Files** (bzw. `Programme`).
   - Fügen Sie den Ordner dort ein (Rechtsklick in einen freien Bereich → **„Einfügen“** oder Tastenkombination `Strg + V`).
   - Bestätigen Sie die Windows-Sicherheitsabfrage („Sie müssen Administratorrechte angeben...“) mit **„Fortsetzen“**.
5. **Ergebnis:** Die Datei `ApE.exe` befindet sich nun im Pfad `C:\Program Files\ApE\ApE.exe`.

### macOS

```bash
brew install --cask ape
```

---

## ImageJ / Fiji

ImageJ (bzw. die erweiterte Distribution Fiji) ist ein Programm für die (semi-automatische) Bildanalyse.

### Windows

Fiji (ImageJ) ist nicht über winget verfügbar. Download unter: [fiji.sc](https://fiji.sc).

**Anleitung für Windows 10 (ZIP entpacken und verschieben):**
1. **Herunterladen:** Laden Sie die Windows 64-bit ZIP-Datei herunter (liegt anschliessend im Ordner *Downloads*).
2. **Entpacken:** Öffnen Sie den Ordner *Downloads*, machen Sie einen **Rechtsklick** auf die ZIP-Datei und wählen Sie **„Alle extrahieren…“**. Klicken Sie im Fenster unten rechts auf **„Extrahieren“**.
3. **Ordner umbenennen:** Machen Sie einen Rechtsklick auf den entpackten Ordner (z. B. `Fiji.app`), wählen Sie **„Umbenennen“** und nennen Sie den Ordner exakt `Fiji`.
4. **Nach `C:\Program Files` verschieben:**
   - Schneiden Sie den Ordner `Fiji` aus (Rechtsklick → **„Ausschneiden“** oder Tastenkombination `Strg + X`).
   - Öffnen Sie im Windows Explorer: **Dieser PC → Lokaler Datenträger (C:) → Program Files** (bzw. `Programme`).
   - Fügen Sie den Ordner dort ein (Rechtsklick in einen freien Bereich → **„Einfügen“** oder Tastenkombination `Strg + V`).
   - Bestätigen Sie die Administratorabfrage mit **„Fortsetzen“**.
5. **Ergebnis:** Die Datei `fiji-windows-x64.exe` befindet sich nun im Pfad `C:\Program Files\Fiji\fiji-windows-x64.exe`.

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

> 💡 **Problemlösung bei Fehler `403 Forbidden` / *„Nicht zulässig“*:**  
> Falls `winget` mit einem 403-Fehler abbricht (aufgrund von Schul-Firewalls, IP-Sperren oder dem DDoS-Schutz des Herstellers), laden Sie GraphPad Prism manuell über den Browser unter [graphpad.com/updates](https://www.graphpad.com/updates) herunter und führen Sie die `.exe`-Datei aus.

Die Aktivierung des Programms erfolgt über eine institutionelle Lizenz. Für den Zugang an die Ansprechpersonen wenden.

### macOS

```bash
brew install --cask prism
```

Download unter: [graphpad.com](https://www.graphpad.com)