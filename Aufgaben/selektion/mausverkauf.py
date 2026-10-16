anzahlMaus = int(input("Anzahl Mäuse eingeben: "))
preis = int(input("Preis eingeben: "))
transportPauschale = 0

if anzahlMaus < 10:
    transportPauschale = 10
else:
    transportPauschale = 0

warenWert = anzahlMaus * preis
netto = warenWert + transportPauschale
steuer = netto / 100 * 19
brutto = netto + steuer

print(f"Der Warenwert beträgt {warenWert} Euro")
print(f"Der Pauschale beträgt {transportPauschale} Euro")
print(f"Fer Nettobetrag beträgt {netto} Euro")
print(f"Die Mehrwertsteuer beträgt {steuer} Euro")
print(f"Der Bruttobetrag beträgt {brutto} Euro")