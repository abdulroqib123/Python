anzahlFlaschen = int(input("Wie viel Flaschen willst du kaufen?: "))
minFlachen = 10
flaschePreis = 3.5
preis = flaschePreis * anzahlFlaschen

if anzahlFlaschen <= minFlachen:
    print(f"Sie haben {preis} zu bezahlen")
elif anzahlFlaschen > minFlachen and anzahlFlaschen <= 50:
    preis = preis - preis * 5 / 100
    print(f"Sie haben {preis} zu bezahlen")
elif anzahlFlaschen > 50:
    preis = preis - preis * 10 / 100
    print(f"Sie haben {preis} zu bezahlen")
else:
    print("Rechnung unmöglich")