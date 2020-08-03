# Luefter
Python-Skript zur Steuerung des PWM-Lüfters eines Jetson Nano, das als cronjob läuft


Das Skript nach /usr/sbin/ kopieren und anschließend die crontab anpassen, indem man

die folgende Zeile hinzufügt:


\*  \*    \* \* \*   root	/usr/sbin/luefter.py


Dies sorgt dafür, dass die Prozessortemperatur minütlich überprüft und die Geschwindigkeit

des Lüfters entsprechend reguliert wird: Der Prozessor bleibt angenehm kühl und arbeitet

auch bei Last performant.

Wer will, mag das Skript seinen Bedürfnissen entsprechend anpassen.


NOCH ZU ERLEDIGEN:

Der Lüfter wird seltsamerweise beim Anhalten des Jetson Nano per shutdown -h now oder über

den entsprechenden Software-Knopf in der grafischen Benutzeroberfläche nicht ausgeschaltet

-- selbst wenn man ein entsprechendes Skript nach /etc/rc0.d/ kopiert! Bei einem Neustart

(reboot) indes funktioniert das Abschalten des Lüfters wie erwartet.