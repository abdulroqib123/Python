netto = int(input("Anzahl Mäuse eingeben: "))

steuer = netto / 100 * 19

brutto = netto + steuer

print(f"Mehrwertsteuer: {steuer}")
print(f"Bruttobetrag: {brutto}")