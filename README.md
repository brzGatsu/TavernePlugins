# TavernePlugins
Dieses Repo ist die offizielle Plugin-Quelle für den Drachentöter-Charaktergenerator Taverne. Plugins und andere Beiträge von anderen Entwicklern sind gerne gesehen, kontaktiert mich einfach auf dem Drachentöter Discord.

## Installationsanleitung

1. Öffne Tavernes Einstellungen über den Zahnrad-Button im Startfenster.
2. Wechsle auf den Tab Plugins
3. Wähle das gewünschte Plugin aus und clicke auf "Installieren".
4. Starte Taverne neu.

## Plugins

### CharakterAssistent
Enthält einen Baukasten mit WdH Spezies, Kulturen und Kämpferprofessionen für Ilaris Advanced

### CharakterToText
Das Plugin sorgt dafür, dass beim beim Speichern des Charakters zusätzlich eine Textdatei im gleichen Ordner angelegt wird. Diese Textdatei enthält alle Charakterwerte in leicht zu kopierendem Format. Ich nutze es beispielsweise, um ein digitales Charaktersheet in Form von Trello-Karten zu befüllen.

### FoundryVTT
Wenn das Plugin aktiv ist, wird beim Speichern des Helden neben der `<name>.xml` automatisch eine zweite Datei `<name>_foundryvtt.json` erstellt, die in Foundry als Held importiert werden kann. Die Foundry Helden können nicht zurück in Taverne importiert werden. Die `.xml`-Datei also nicht löschen!

Es werden nur die für FoundryVTT relevanten Informationen in der `.json`-Datei gespeichert und auch hier gibt es noch einige Einschränkungen. Folgendes wird NICHT übertragen:

- Geld
- Zustände: Wunden, Furcht, Boni/Mali etc.
- Status von Waffen/Rüstungen (in/aktiv, haupthand/nebenhand, kampfstil)
- Einstellungen für Taverne (Welcher Bogen, Zonensystem, Regelanhänge usw..)
- Hausregeln (Eigene Vorteile, Talente usw. könnten aber funktionieren)
- Waffeneigenschaften

### Historie
In der Historie werden Änderungen des Charakters in Textform gespeichert. Über einen Extra-Tab im Charakter-Editor lässt sich der EP Verlauf und die Änderungen von übernatürlichen, freien und profanen Fertigkeiten und Talenten, Eigenheiten, Zaubern, Vorteilen und Attributen nach verfolgen. Das Inventar und Beschreibungen, die nicht ausschlaggebend für die Generierung sind, werden nicht aufgezeichnet.

Aus dem aufgezeichneten Verlauf ist es nicht möglich alte Versionen des Charakters wieder herzustellen. Zu diesem Zweck bietet das Plugin jedoch die Möglichkeit automatische Backups nach EP-Stand oder Datum anzulegen. Verschiedene Dateien können mit dem charakter_diff-Makro verglichen werden.

### Kreaturen
Mit dem Kreaturen Plugin können neben Charakteren auch Kreaturen als Gegner oder NSCs erstellt werden. Die Generierung ist weniger kompliziert und folgt keinen Regeln. Fertige Kreaturen können als Statblock exportiert oder mit dem IlarisOnline Plugin auf ilaris-online.de veröffentlicht werden.

### SephMakro
SephMakro bietet eine einfache Art, Abfragen oder Analysen der Datenbank oder von Charakteren durchzuführen. Die Einstiegshürde ist deutlich niedriger, als für jede noch so kleine Abfrage ein eigenes Plugin schreiben zu müssen. Durch die Verfügbarkeit von Datenbank und Charakteren in Form der Taverne-Datenstrukturen können diese schneller und einfacher durchgeführt werden als wenn erst einmal die XML-Dateien geparst werden müssten. Makros sind aber keine Grenzen gesetzt, es können beispielsweise auch Charaktere verändert und gespeichert werden. Für das Nutzen von vorgefertigten Makros benötigst du in der Regel keine Programmierkenntnisse.

Features:
- Enthält einen Code-Editor mit Zeilen-Anzeige und Syntax-Highlighting. Der Editor hat auch eine rudimentäre Autocomplete-Funktion, die allerdings keinen Kontext kennt.
- Alle Taverne-Python-Files können importiert werden, ihr könntet mit einem Makro theoretisch sogar den Charaktereditor nachprogrammieren.
- Der print output und eventuelle Fehler wird direkt in einem Textfeld angezeigt. 
- Auf die Datenbank kannst du direkt über die globale Variable "datenbank" zugreifen. Sie hat für jedes Datenbankelement ein dict<name, objekt> als Attribut. So kannst du beispielsweise mit datenbank.vorteile["Achaz"] an das Objekt des Vorteils "Achaz" gelangen. Die Struktur der Datenbankobjekte kannst du hier nachschlagen: https://github.com/Aeolitus/Taverne/tree/master/src/Sephrasto/Core.
- Außer Taverne und diesem Plugin wird nichts benötigt!

#### SephMakroScripts
Hier findest du einige nützliche scripts für Sephmakro.
- charakter_diff: Das Makro gibt den Unterschied zwischen zwei Charakterversionen aus. Die Idee ist, dass ihr nach jedem Steigern eine neue Datei für euren Charakter anlegt - mit diesem Makro erhaltet ihr dann eine Historie.
- drachentoeter_simulator: Dies ist eine Simulation für die Drachentöter-Kampfregeln hauptsächlich zum Testen des Balancings. Drachentöter kann hier gefunden werden: https://dsaforum.de/viewtopic.php?t=59615
- fertigkeiten_sf: Rechnet bei allen Fertigkeiten für alle Traditionen die Talentkosten zusammen, bildet den Durchschnitt und gibt den Steigerungsfaktor gemäß Ilaris Blog aus. Passive Talente werden ignoriert (da PW-unabhängig) und Traditionen mit 100 oder weniger investierbaren EP werden ignoriert. Es gibt hier einige Einstellungsmöglichkeiten direkt am Anfang des Makros.
- inselfertigkeiten: Das Makro betrachtet für jede Tradition alle Fertigkeiten, deren Talent-Gesamt-EP unter 121 liegen. Dann inspiziert es jedes Talent dieser Fertigkeiten und prüft, ob es mit einer anderen Fertigkeit oberhalb der EP-Schwelle wirkbar ist. Wird ein Talent gefunden, bei dem das nicht der Fall ist, wird es zusammen mit seiner "Inselfertigkeit" ausgegeben. Passive Talente werden ignoriert (da PW-unabhängig). Es gibt hier einige Einstellungsmöglichkeiten direkt am Anfang des Makros
- talent_seitenzahlen_update: Das Makro aktualisiert die Seitenzahl-Angaben von übernatürlichen Talenten in der Taverne-Datenbank. Dazu werden die Lesezeichen einer gewählten PDF-Datei ausgewertet. Diese müssen exakt gleich, wie die Talente heißen. PDFs ohne Talentnamen in den Lesezeichen werden nicht unterstützt!
- waffenbewerter: Das Makro geht durch alle Waffen in der Datenbank und wendet ein Punkteschema an (ähnlich wie hier: https://dsaforum.de/viewtopic.php?f=180&t=56989&p=2012837#p2012837), wodurch Waffen besser verglichen werden können. Das hilft insbesondere dabei, eigene Waffenkreationen zu balancen. Das Standard-Bewertungsschema habe ich nach bestem Gewissen erstellt, ich erhebe keinen Anspruch auf Richtigkeit, das kann nur Curthan :D. Das Schema ist sehr einfach komplett einstellbar in der Settings-Sektion.
- zufälligeZauber: Das Makro würfelt auf die Verbreitungsangabe aller Zauber für eine angegebene Tradition.
- zufälligeZauberNumpy: Wie zufälligeZauber mit etwas anderer Wahrscheinlichkeitsverteilung, aber benötigt Python und das Paket Numpy.

### Tierbegleiter
Dieses Plugin erlaubt das Erstellen von Tierbegleitern entsprechend des Ilaris Bestiariums und das Exportieren in den enthaltenen Tierbegleiterbogen. Optional können in der Regelbasis mittels der Einstellung "Tierbegleiter Plugin: IA Zucht und Ausbildung" die Ilaris Advanced Regeln zu Zucht und Ausbildung aktiviert werden (zusammen mit speziell angepassten Tierwerten).

## Templates für Plugin-Entwickler

### DBToText
Das Plugin kann als Template für Datenbankexporter dienen. Es speichert die Datenbank in einer Textdatei.