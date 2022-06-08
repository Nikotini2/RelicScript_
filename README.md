Unter den Datein finden Sie eine .py und .txt (RelicScript.txt) Datei welche beide den Code der Anwendung enthalten (die .txt ist zur Absicherung da, falls die .py nicht funktionieren sollte). Zu dem ist auch die fertige .exe Datei beigelegt, welche nur aus dem Verzeichnis heraus ausgeführt werden sollte.

Das Projekt an sich ist im Grunde funktionsfähig, da nur ein paar optische Verbesserungen gemacht werden müssen und ein paar kleine features wie erweiterte Einstellungen in Planung sind/waren.

Zur Anwendung:
Sobald Sie die Anwendung starten ist diese ausgeschaltet und kann mit einem Klick angeschaltet werden. Daneben ist der Timer zu sehen, welcher bei 0 den Bildschirm auf Relikte scannt. Darunter befindet sich ein Eingabefeld, der Button "Add New Relic" und ein Drop down menu. Diese sind dazu da um Relikte manuell hinzufügen zu können.
Ein Reliktname in Warframe besteht immer aus zwei Teilen:
1. Eine von vier Bezeichnungen (Axi, Lith, Meso und Neo), welche die Art des RElikts bestimmen.
2. Einem Buchstaben und einer Zahl (meistens 1 bis 18).

Ein Reliktname würde z.B. so aussehen: "Meso B11"
Um ein Relikt hinzu zu fügen wählt man einfach die Art des Relikts im Drop down menu aus und schreibt dessen Bezeichnugn (z.B. B11) in das Eingabefeld dahinter und klickt auf "Add New Relic"
Die Anwendung verfügt auch über eine Speichern und Laden Funktion. Dazu dienen die "Save" und "Load" Buttons. Im Verzeichnis der Anwendung befindet sich eine Textdatei namens relicsave.txt. Dies ist eine Beispiel Sicherung und auch die Textdatei in welcher die Relikte gespeichert werden wenn man "save" drückt. Unter den zwei Buttons wird angezeigt welches Relikt als letztes gefunden wurde (daher auch "nothing yet"). Rechts daneben befinden sich vier Buttons welche die vier Reliktarten zeigen. Diese Buttons sind dafür da um die Liste nach einer Art Relikt zu sortieren. Darunter kann man den Timer einstellen (Eingabe in Sekunden). Rechts über eben erwähnten Eingabefeld für den Timer steht eine kleine null. Dies ist ein Feature welches noch nicht in die UI implementiert wurde. Hierbei handelt es sich einfach um einen Cooldown für den Timer nachdem ein Relikt gefunden wurde um fälschliche Doppeleinträge zu vermeiden.

Ich habe für die Demonstrierung den Input für den "Scanner" dauerhaft auf die Datei "relic coords.png" gesetzt. Normalerweise würde ein Bild vom Bildschirm in scanpic.png gespeichert werden und diese Datei als Input genutzt werden. (Zeile 116 und 117 im Code). Leider kann ich Ihnen dieses Feature nicht vorführen, da die benötigten Datein für die Texterkennung zu groß und zu viele sind. Die verwendete OCR heißt übrigens "pytesseract".
