anzahlMaus = int(input("Anzahl Mäuse eingeben: "))
preis = int(input("Winzelpreis eingeben: "))

netto = anzahlMaus * preis

steuer = netto / 100 * 19

brutto = netto + steuer

print(f"Nettobetrag: {netto}")
print(f"Mehrwertsteuer: {steuer}")
print(f"Bruttobetrag: {brutto}")