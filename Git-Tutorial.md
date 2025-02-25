# Git Tutorial

## Git installieren
[Link zu Git Homepage](https://git-scm.com/)
- installieren von git für Window
- macOS und Linux sollten bereits mit vorinstalliertem Git kommen

## Git einrichten
- git config konfigurieren

- überprüfen ob config eingerichtet ist
```bash
git config --list
```
- mindestens E-mail und User-Name muss eingerichtet werden

```bash
# User Name erstellen
git config --global user.name "<Your Name>"

# E-Mail erstellen
git config --global user.email "<your email address>"
```
optional direkt immer `main` als Haupt-Branch festlegen
```bash
git config --global init.defaultBranch <name>
```
## Repository initialisieren
```bash
git init
```
wenn ihr nur diesen Befehl eingebt und nicht vorher Git gesagt habt, dass der Hauptbranch main heißen soll wird der Hauptbranch master sein.

um das zu ändern müsst ihr NACH des init Befehls folgenden Befehl ausführen:
```bash
git branch -m main
```
um direkt bei der Initialisierung den Hauptbranch `main` zu nennen:
```bash
git init -b main
```
Status des neuen Repositories und überhaupt zu prüfen
```bash
git status
```
## Dateien tracken bzw. zu Staging hinzufügen
- Datei im Arbeitsverzeichnis anlegen und mittels Git command tracken
```bash
git add <name_der_datei_mit_endung>
```
- wenn mehrere Dateien zu tracken bzw. zum Staging hinzugefügt werden sollen
```bash
git add .
```
- Datei wieder aus der Staging-Ebene entfernen
```bash
git rm --cached <name_der_datei>
```
## Der erste Commit
- mit einem Commit werden alle Dateien, welche sich gerade im Staging befinden in das lokale Repository (Storage), mit dem aktuellen Staging Zustand, aufgenommen
```bash
git commit -m "<Deine Commit Message>"
```
## Der zweite Commit
- lege eine neue Datei Deiner Wahl an und füge diese zum Staging hinzu mit `git add` und commite anschließen diese neuen Stand Deines Arbeitsverzeichnisses
