bestellWert = int(input("Gib die Bestellwert ein: "))
pauschale = 5.5

if bestellWert < 200:
    print(f"Den Rechnungbetrag ist {bestellWert + pauschale} Euro")
else:
    print(f"Den Rechnungbetrag ist {bestellWert} Euro")
