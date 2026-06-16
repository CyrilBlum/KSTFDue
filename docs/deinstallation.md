---
layout: default
title: Deinstallation
nav_order: 5
---

# Deinstallation (brew / winget)

Mit den folgenden Befehlen können installierte Programme sauber entfernt werden.

> **Hinweis:** Führen Sie die Befehle nur für Programme aus, die wirklich entfernt werden sollen.

---

## Windows (winget)

Öffnen Sie **PowerShell als Administrator** und verwenden Sie:

### Einzelnes Programm entfernen

```powershell
winget uninstall --id Microsoft.VisualStudioCode -e
```

Weitere Beispiele:
```powershell
winget uninstall --id ETHZurich.SafeExamBrowser -e
winget uninstall --id Python.Python.3.13 -e
winget uninstall --id Musescore.Musescore -e
winget uninstall --id BlenderFoundation.Blender -e
winget uninstall --id Adobe.CreativeCloud -e
```

### Mehrere Programme auf einmal entfernen

```powershell
$apps = @(
  "Microsoft.VisualStudioCode",
  "ETHZurich.SafeExamBrowser",
  "Python.Python.3.13",
  "Musescore.Musescore",
  "BlenderFoundation.Blender"
)

foreach ($id in $apps) {
  winget uninstall --id $id -e
}
```

### Installierte Programme anzeigen

```powershell
winget list
```

---

## macOS (Homebrew)

Öffnen Sie ein Terminal (*Cmd + Leertaste → „Terminal"*) und verwenden Sie:

### Einzelnes Programm entfernen

```bash
brew uninstall --cask visual-studio-code
```

Weitere Beispiele:
```bash
brew uninstall --cask safe-exam-browser
brew uninstall --cask fiji
brew uninstall --cask musescore
brew uninstall --cask blender
brew uninstall --cask ape
brew uninstall --cask cellprofiler
brew uninstall --cask mega
brew uninstall --cask prism
brew uninstall --cask geogebra
brew uninstall --cask adobe-creative-cloud
```

### Python (falls via Homebrew installiert)

```bash
brew uninstall python@3.13
```

### Mehrere Programme auf einmal entfernen

```bash
brew uninstall --cask visual-studio-code safe-exam-browser fiji musescore blender
```

### Aufräumen

Die folgenden beiden Befehle entfernen ungenutzte Abhängigkeiten, bereinigen den Cache und entfernen alte Versionen:

```bash
brew autoremove
brew cleanup
```

### Installierte Pakete anzeigen

Die folgenden beiden Befehle zeigen die installierten Homebrew-Pakete an (casks, also Programme, und formulas, also Kommandozeilen-Tools, ohne deren *dependencies*):
```bash
brew list --cask
brew leaves
```

---

## Manuell installierte Programme

Einige Tools wurden eventuell **nicht** über brew/winget installiert (z. B. ApE, CellProfiler, MEGA, Filius je nach Setup).  
Diese Programme müssen manuell entfernt werden:

- **macOS:** App aus `/Applications` in den Papierkorb ziehen.
- **Windows:** *Einstellungen → Apps → Installierte Apps* und dort deinstallieren.

## Deinstallation aller Tools auf einmal

### Windows (winget)

```powershell
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Deinstallation aller Tools – Windows"   -ForegroundColor Cyan
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

foreach ($id in $apps) {
  winget uninstall --id $id -e --accept-source-agreements
  if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ entfernt: $id" -ForegroundColor Green
  } else {
    Write-Host "ℹ️ übersprungen/nicht installiert: $id" -ForegroundColor Yellow
  }
}

Write-Host ""
Write-Host "Fertig. Manuell installierte Programme ggf. separat entfernen." -ForegroundColor Cyan
```

### macOS (Homebrew)

```bash
echo "========================================"
echo " Deinstallation aller Tools – macOS"
echo "========================================"
echo ""

casks=(
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
  filius
  geogebra
  musescore
)

formulas=(
  python@3.13
)

for p in "${casks[@]}"; do
  brew uninstall --cask "$p" >/dev/null 2>&1 && echo "✅ entfernt: $p" || echo "ℹ️ übersprungen/nicht installiert: $p"
done

for p in "${formulas[@]}"; do
  brew uninstall "$p" >/dev/null 2>&1 && echo "✅ entfernt: $p" || echo "ℹ️ übersprungen/nicht installiert: $p"
done

brew autoremove
brew cleanup

echo ""
echo "Fertig. Manuell installierte Programme ggf. separat entfernen."
```