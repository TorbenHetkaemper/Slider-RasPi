# Slider-RasPi
Beschreibung des Slider-Projekts:
1. Initialisierungsfahrt mittels Joystick (in x-Achse), um den Start- und Endpunkt festzulegen.
2. Bestätigung der eingabe durch Knopfdruck des Joysticks.
3. Einstellung der Geschwindigkeit der Fahrt mittels Joystick (y-Richtung).
4. Bestätigung der eingabe durch Knopfdruck des Joysticks.
5. Fahrt beginnt.

Optional:
In weiteren Schritten kann eine Menüauswahl geplant werden, die es ermöglicht unterschiedliche Slidermodis zu wählen.
Ein Modi wäre die kontinuierliche Kamerafahrt; wie oben beschrieben und ein zusätzlicher währe die SMS-Fahrt (Shot-Move-Shot) für Foto-Timelapse.

SMS:
1. Man initialisiert wieder die Eckpunkte s.O.
2. Man stellt die gewünschte Dauer der Timelapse ein.
3. Wieder die Bestätigung durch Knopfdruck.
4.Fahrt beginnt, d.h. die Kamera macht ein Bild, fährt dann ein Stück, hält an und macht das nächste Bild usw. bis zum Endpunkt.

# Bauteile
Variante 1 (Kamerafahrt):
- Raspberry Pi
- Motorshield
- Joystick (KY-023)
- ADC (ADS 1115)
- 3,5" Touch Display

Variante 2 (Foto-Timelapse):
- Raspberry Pi
- Motorshield
- Joystick (KY-023)
- ADC (ADS 1115)
- 3,5" Touch Display
- IR-Emitter
