---
layout: default
title: ⭐ Installationscheck
parent: Kurzzeitgymnasium (KG)
nav_order: 2
---

# KG Installationscheck

Mit den folgenden Skripten kann überprüft werden, ob alle Programme korrekt installiert wurden. Das passende Skript je nach Betriebssystem ausführen.

---

## Windows

Öffnen Sie **PowerShell als Administrator** (*Windows-Taste → „PowerShell" → Rechtsklick → „Als Administrator ausführen"*) und führen Sie folgenden Befehl aus:

```powershell
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " KG Installationscheck – Windows"       -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$ok   = 0
$fail = 0

function Check-Winget {
    param([string]$Label, [string]$Id)
    $result = winget list --id $Id --accept-source-agreements 2>&1
    if ($result -match [regex]::Escape($Id)) {
        Write-Host "✅  $Label" -ForegroundColor Green
        $script:ok++
    } else {
        Write-Host "❌  $Label – nicht installiert (winget-ID: $Id)" -ForegroundColor Red
        $script:fail++
    }
}

function Check-Path {
    param([string]$Label, [string]$ExePath)
    if (Test-Path $ExePath) {
        Write-Host "✅  $Label" -ForegroundColor Green
        $script:ok++
    } else {
        Write-Host "❌  $Label – nicht gefunden ($ExePath)" -ForegroundColor Red
        $script:fail++
    }
}

function Check-Glob {
    param([string]$Label, [string]$GlobPattern)
    $found = Get-Item $GlobPattern -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($found) {
        Write-Host "✅  $Label" -ForegroundColor Green
        $script:ok++
    } else {
        Write-Host "❌  $Label – nicht gefunden ($GlobPattern)" -ForegroundColor Red
        $script:fail++
    }
}

function Check-Command {
    param([string]$Label, [string]$Cmd)
    if (Get-Command $Cmd -ErrorAction SilentlyContinue) {
        Write-Host "✅  $Label" -ForegroundColor Green
        $script:ok++
    } else {
        Write-Host "❌  $Label – nicht gefunden (Befehl: $Cmd)" -ForegroundColor Red
        $script:fail++
    }
}

Write-Host "--- Alle Fächer ---"
Check-Winget "SafeExamBrowser"      "ETHZurich.SafeExamBrowser"

Write-Host ""
Write-Host "--- Bildnerisches Gestalten ---"
Check-Winget "Adobe Creative Cloud" "Adobe.CreativeCloud"
Check-Winget "Blender"              "BlenderFoundation.Blender"

Write-Host ""
Write-Host "--- Biologie ---"
Check-Path     "Fiji (ImageJ)"        "$env:ProgramFiles\Fiji\fiji-windows-x64.exe"
Check-Path     "ApE"                  "$env:ProgramFiles\ApE\ApE.exe"
Check-Path     "CellProfiler"         "$env:ProgramFiles\CellProfiler\CellProfiler.exe"
Check-Winget   "MEGA"                 "iGEM.MEGA.12"
Check-Winget   "GraphPad Prism"       "GraphPad.Prism"

Write-Host ""
Write-Host "--- Informatik ---"
Check-Winget "VS Code"              "Microsoft.VisualStudioCode"
Check-Winget "Python 3"             "Python.Python.3.13"
Check-Winget   "Filius"              "StefanFreischlad.Filius"

Write-Host ""
Write-Host "--- Mathematik ---"
Check-Winget "GeoGebra"             "GeoGebra.Classic"

Write-Host ""
Write-Host "--- Musik ---"
Check-Winget "MuseScore"            "Musescore.Musescore"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Ergebnis: $ok ✅  installiert, $fail ❌  fehlend" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
```

> **Hinweis:** Das Skript kann direkt in PowerShell eingefügt und ausgeführt werden. Programme, die nur als Download verfügbar sind (ApE, CellProfiler, MEGA usw.), werden anhand ihres Standard-Installationspfades geprüft – der Pfad kann je nach Version oder Installationsort leicht abweichen.

---

## macOS

Öffnen Sie ein Terminal (*Cmd + Leertaste → „Terminal"*) und führen Sie folgenden Befehl aus:

```bash
echo "========================================"
echo " KG Installationscheck – macOS"
echo "========================================"
echo ""

ok=0
fail=0

check_cmd() {
  local label="$1"
  local cmd="$2"
  if command -v "$cmd" &>/dev/null; then
    echo "✅  $label"
    ok=$((ok + 1))
  else
    echo "❌  $label – nicht gefunden (Befehl: $cmd)"
    fail=$((fail + 1))
  fi
}

check_cask() {
  local label="$1"
  local cask="$2"
  if brew list --cask "$cask" &>/dev/null 2>&1; then
    echo "✅  $label"
    ok=$((ok + 1))
  else
    echo "❌  $label – nicht installiert (brew cask: $cask)"
    fail=$((fail + 1))
  fi
}

check_app() {
  local label="$1"
  local app_path="$2"
  if [ -d "$app_path" ]; then
    echo "✅  $label"
    ok=$((ok + 1))
  else
    echo "❌  $label – nicht gefunden ($app_path)"
    fail=$((fail + 1))
  fi
}

check_app_pattern() {
  local label="$1"
  local pattern="$2"
  if find /Applications -maxdepth 1 -name "$pattern" -type d 2>/dev/null | grep -q .; then
    echo "✅  $label"
    ok=$((ok + 1))
  else
    echo "❌  $label – nicht gefunden (/Applications/$pattern)"
    fail=$((fail + 1))
  fi
}

echo "--- Alle Fächer ---"
check_cmd   "Homebrew"             "brew"
check_cask  "Microsoft Office"     "microsoft-office"
check_cask  "SafeExamBrowser"      "safe-exam-browser"
check_cask  "rectangle"            "rectangle"

echo ""
echo "--- Informatik ---"
check_cask  "VS Code"              "visual-studio-code"
check_cmd   "Python 3"             "python3"
check_app   "Filius"               "/Applications/Filius.app"

echo ""
echo "--- Biologie ---"
check_cask  "Fiji (ImageJ)"        "fiji"
check_app   "ApE"                  "/Applications/ApE.app"
check_app   "CellProfiler"         "/Applications/CellProfiler.app"
check_app_pattern "MEGA"           "MEGA*.app"
check_app_pattern "GraphPad Prism" "Prism*.app"

echo ""
echo "--- Mathematik ---"
check_app   "GeoGebra"             "/Applications/GeoGebra Classic 6.app"

echo ""
echo "--- Musik ---"
check_cask  "MuseScore"            "musescore"

echo ""
echo "--- Bildnerisches Gestalten ---"
check_cask  "Adobe Creative Cloud" "adobe-creative-cloud"
check_cask  "Blender"              "blender"

echo ""
echo "========================================"
echo " Ergebnis: $ok ✅  installiert, $fail ❌  fehlend"
echo "========================================"
```

> **Hinweis:** Das Skript kann direkt in das Terminal kopiert und mit der Eingabetaste ausgeführt werden. Programme, die nur als Download verfügbar sind (ApE, CellProfiler usw.), werden anhand ihres Installationspfades geprüft – der Pfad kann je nach Version leicht abweichen.
