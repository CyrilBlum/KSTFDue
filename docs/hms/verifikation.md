---
layout: default
title: ⭐ Installationscheck
parent: Handelsmittelschule (HMS)
nav_order: 2
---

# HMS Installationscheck

Mit den folgenden Skripten kann überprüft werden, ob alle Programme für die HMS korrekt installiert wurden. Das passende Skript je nach Betriebssystem ausführen.

---

## Windows

Öffnen Sie **PowerShell als Administrator** (*Windows-Taste → „PowerShell" → Rechtsklick → „Als Administrator ausführen"*) und führen Sie folgenden Befehl aus:

```powershell
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " HMS Installationscheck – Windows"      -ForegroundColor Cyan
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

Write-Host "--- Allgemein ---"
Check-Winget "SafeExamBrowser"      "ETHZurich.SafeExamBrowser"

Write-Host ""
Write-Host "--- Bildnerisches Gestalten ---"
Check-Winget "Adobe Creative Cloud" "Adobe.CreativeCloud"
Check-Winget "Blender"              "BlenderFoundation.Blender"

Write-Host ""
Write-Host "--- Biologie ---"
Check-Winget   "MEGA"                 "iGEM.MEGA.12"
Check-Winget   "GraphPad Prism"       "GraphPad.Prism"

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

> **Hinweis:** Das Skript kann direkt in PowerShell eingefügt und ausgeführt werden.

---

## macOS

Öffnen Sie ein Terminal (*Cmd + Leertaste → „Terminal"*) und führen Sie folgenden Befehl aus:

```bash
echo "========================================"
echo " HMS Installationscheck – macOS"
echo "========================================"
echo ""

ok=0
fail=0

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

echo "--- Allgemein ---"
check_cask  "SafeExamBrowser"      "safe-exam-browser"
check_cask  "Rectangle"            "rectangle"

echo ""
echo "--- Bildnerisches Gestalten ---"
check_cask  "Adobe Creative Cloud" "adobe-creative-cloud"
check_cask  "Blender"              "blender"

echo ""
echo "--- Biologie ---"
check_app_pattern "MEGA"           "MEGA*.app"
check_app_pattern "GraphPad Prism" "Prism*.app"

echo ""
echo "--- Mathematik ---"
check_app   "GeoGebra"             "/Applications/GeoGebra Classic 6.app"

echo ""
echo "--- Musik ---"
check_cask  "MuseScore"            "musescore"

echo ""
echo "========================================"
echo " Ergebnis: $ok ✅  installiert, $fail ❌  fehlend"
echo "========================================"
```

> **Hinweis:** Das Skript kann direkt in das Terminal kopiert und mit der Eingabetaste ausgeführt werden.
