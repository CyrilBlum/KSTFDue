---
layout: default
title: ⭐ Schnellinstallation
parent: Kurzzeitgymnasium (KG)
nav_order: 1
---

# KG Schnellinstallation

Diese Seite bündelt die wichtigsten Installationsschritte in je **einem Block für Windows** und **einem Block für macOS**.

Diese Schnellinstallation ist speziell auf die Bedürfnisse des Kurzzeitgymnasiums (KG) zugeschnitten und enthält alle Programme, die für die meisten Fachschaften relevant sind. Sie bietet eine effiziente Möglichkeit, die benötigte Software mit minimalem Aufwand zu installieren.

Die Codeblöcke können einfach kopiert werden, indem Sie auf das Symbol (📋) im oberen rechnten Teil des Code-Blocks klicken. Danach können Sie den Code-Block per Cmd+V / Ctrl+V im Terminal bzw. PowerShell einfügen und mit Enter ausführen.

Die Schnellinstallation kann je nach System und Internetverbindung einige Minuten bis zu über einer Stunde dauern.

---

## Windows (winget)

Öffnen Sie **PowerShell als Administrator** und führen Sie den gesamten Block aus.

```powershell
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Schnellinstallation – Windows"         -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$apps = @(
  "ETHZurich.SafeExamBrowser",
  "Adobe.CreativeCloud",
  "BlenderFoundation.Blender",
  "iGEM.MEGA.12",
  "GraphPad.Prism",
  "Microsoft.VisualStudioCode",
  "Python.Python.3.13",
  "StefanFreischlad.Filius",
  "GeoGebra.Classic",
  "Musescore.Musescore"
)

$ok = 0
$fail = 0

foreach ($id in $apps) {
  Write-Host "Installiere $id ..."
  winget install --id $id -e --accept-package-agreements --accept-source-agreements --silent
  if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ $id" -ForegroundColor Green
    $ok++
  } else {
    Write-Host "❌ $id" -ForegroundColor Red
    $fail++
  }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Ergebnis: $ok ✅  erfolgreich, $fail ❌  fehlgeschlagen" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
```

Achtung: nicht alle Programme sind über winget verfügbar. Alle Programme, die nicht über winget installiert werden können, müssen manuell installiert werden:
- **ApE**: Download unter [jorgensen.biology.utah.edu/wayned/ape](https://jorgensen.biology.utah.edu/wayned/ape). Nach dem Download: Das heruntergeladene `zip`-Archiv entpacken, den Ordner in `ApE` umbenennen und diesen, sowie dessen Inhalt, in `C:\Program Files\ApE` verschieben.
- **CellProfiler**: Download unter [cellprofiler.org](https://cellprofiler.org). Exe-Datei herunterladen, anklicken und das Programm installieren.
- **ImageJ / Fiji**: Download unter [fiji.sc](https://fiji.sc). Nach dem Download: Die heruntergeladene `zip`-Datei entpacken, den Ordner in `Fiji` umbenennen und diesen, sowie dessen Inhalt, in `C:\Program Files\Fiji` verschieben.

---

## macOS (Homebrew)

Öffnen Sie Terminal und führen Sie den gesamten Block aus.

Sie müssen sich gegebenenfalls durch die Eingabe Ihres Passworts authentifizieren. Das gewöhnliche Passwort Ihres MacOS-Benutzerkontos ist gemeint, nicht das Apple-ID-Passwort.

```bash
echo "========================================"
echo " Schnellinstallation – macOS"
echo "========================================"
echo ""

# Homebrew prüfen
if ! command -v brew >/dev/null 2>&1; then
  echo "❌ Homebrew fehlt. Bitte zuerst installieren: https://brew.sh"
  exit 1
fi

brew update

# Formulas
formulas=(
  python3
)

# Casks
casks=(
  microsoft-office
  safe-exam-browser
  rectangle
  adobe-creative-cloud
  blender
  ape
  fiji
  cellprofiler
  mega
  prism
  visual-studio-code
  geogebra
  musescore
)

ok=0
fail=0

install_formula () {
  local pkg="$1"
  if brew list "$pkg" >/dev/null 2>&1; then
    echo "✅ $pkg bereits installiert"
    ok=$((ok + 1))
  elif brew install "$pkg"; then
    echo "✅ $pkg installiert"
    ok=$((ok + 1))
  else
    echo "❌ $pkg fehlgeschlagen"
    fail=$((fail + 1))
  fi
}

install_cask () {
  local pkg="$1"
  if brew list --cask "$pkg" >/dev/null 2>&1; then
    echo "✅ $pkg bereits installiert"
    ok=$((ok + 1))
  elif brew install --cask "$pkg"; then
    echo "✅ $pkg installiert"
    ok=$((ok + 1))
  else
    echo "❌ $pkg fehlgeschlagen"
    fail=$((fail + 1))
  fi
}

echo "--- Formulas ---"
for p in "${formulas[@]}"; do install_formula "$p"; done

echo ""
echo "--- Casks ---"
for p in "${casks[@]}"; do install_cask "$p"; done

echo ""
echo "========================================"
echo " Ergebnis: $ok ✅  erfolgreich, $fail ❌  fehlgeschlagen"
echo "========================================"
```

Filius ist unter macOS nicht über Homebrew verfügbar und muss separat installiert werden:

[lernsoftware-filius.de](https://www.lernsoftware-filius.de)

Die macOS-Version herunterladen und installieren.
