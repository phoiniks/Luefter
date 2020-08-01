# Luefter
Python-Skript zur Steuerung des PWM-Lüfters eines Jetson Nano, das als cronjob läuft

Das Skript nach /usr/sbin/ kopieren und anschließend die crontab anpassen, indem man

die folgende Zeile hinzufügt:

*  *    * * *   root	/usr/sbin/luefter.py

Dies sorgt dafür, dass die Prozessortemperatur minütlich überprüft und die Geschwindigkeit

des Lüfters entsprechend reguliert wird: Der Prozessor bleibt angenehm kühl und arbeitet

performant.

Wer will, mag das Skript seinen Bedürfnissen entsprechend anpassen.