---
layout: default
title: Homebrew
nav_order: 2
---

# Homebrew (nur macOS)

Homebrew ist der Paketmanager für macOS. Er wird für alle weiteren Installationen auf macOS vorausgesetzt und muss zuerst eingerichtet werden. Hierzu benötigen Sie Administratorrechte auf Ihrem MacOS-Benutzerkonto.

**Windows-Nutzer/-innen:** Diese Seite ist nicht relevant – bitte direkt zu den fachspezifischen Installationsseiten wechseln.

Die Codeblöcke können einfach kopiert werden, indem Sie auf das Symbol (📋) im oberen rechnten Teil des Code-Blocks klicken. Danach können Sie den Code-Block per Cmd+V im Terminal bzw. PowerShell einfügen und mit Enter ausführen.

---

## Installation

Öffnen Sie ein Terminal (*Cmd + Leertaste → „Terminal"* eingeben und öffnen) und führen Sie folgenden Befehl aus:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Das Installationsskript führt durch den gesamten Prozess. Administratorrechte (macOS-Passwort) werden benötigt. Sie müssen sich gegebenenfalls durch die Eingabe Ihres Passworts authentifizieren. Das gewöhnliche Passwort Ihres MacOS-Benutzerkontos ist gemeint, nicht das Apple-ID-Passwort.

---

## PATH-Konfiguration (Apple Silicon, d.h. M1/M2/M3/M4)

Auf neueren Macs mit Apple-Silicon-Chip installiert Homebrew standardmässig nach `/opt/homebrew`. Nach der Installation erscheint im Terminal ein Hinweis wie:

```
==> Next steps:
- Run these commands in your terminal to add Homebrew to your PATH:
    echo >> /Users/<benutzername>/.zprofile
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/<benutzername>/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
```

Diesen Block kopieren (**nicht den obigen, sondern den im Terminal angezeigten**) und ebenfalls im Terminal ausführen. 

Achten Sie sich darauf, **nur die unteren drei Zeilen** zu kopieren, nicht die Zeile mit „echo >> ...“ am Anfang.

Danach das Terminal neu starten.

---

## Überprüfen der Installation

Nach der Installation prüfen, ob Homebrew korrekt eingerichtet ist:

```bash
brew --version
```

Es sollte eine Ausgabe wie `Homebrew 4.x.x` erscheinen.

---

## Homebrew aktuell halten

Vor der Installation weiterer Programme empfiehlt es sich, Homebrew zu aktualisieren:

```bash
brew update
```
