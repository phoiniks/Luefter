# Luefter
Python-Skript zur Steuerung des PWM-Lüfters eines Jetson Nano, das als cronjob läuft


Das Skript nach /usr/sbin/ kopieren und anschließend die crontab anpassen, indem man

die folgende Zeile hinzufügt:


\*  \*    \* \* \*   root	/usr/sbin/luefter.py


Dies sorgt dafür, dass die Prozessortemperatur minütlich überprüft und die Geschwindigkeit

des Lüfters entsprechend reguliert wird: Der Prozessor bleibt angenehm kühl und arbeitet

auch bei Last performant.

Wer will, mag das Skript seinen Bedürfnissen entsprechend anpassen.



Do 6. Aug 22:29:08 CEST 2020

luefter.sh übernimmt das Abschalten des Lüfters bei Neustart und Abschalten des Computers.

Sinnvoll ist das Anlegen eines symbolischen Links, indem man das Skript etwa nach /etc/init.d/

kopiert und von dort aus nach /etc/rc0.d/ (Abschalten) und /etc/rc6.d/ (Neustart) symbolisch

verlinkt, etwa:

ln -s /etc/init.d/luefter.sh /etc/rc0.d/K00AAAA_Luefter

bzw.

ln -s /etc/init.d/luefter.sh /etc/rc6.d/K00AAAA_Luefter

