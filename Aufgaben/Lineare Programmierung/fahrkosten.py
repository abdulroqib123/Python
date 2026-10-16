fahrtpreis = int(input("Gib den Preis der Klassenfahrt ein: "))
anzahlSchüler = int(input("Gib der Anzahl der Schüler ein: "))
anzahlBegleitPersonen = int(input("Gib der Anzahl der Begleitpersonen ein: "))

fahrKosten = fahrtpreis * anzahlSchüler + fahrtpreis * anzahlBegleitPersonen

print(f"Die Fahrkosten fuer die gesamte Klasse betragen {fahrKosten} Euro")