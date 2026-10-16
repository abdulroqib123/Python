längeA = float(input("BItte geben sie sie Seitenlänge A ein (in cm): "))
längeB = float(input("BItte geben sie sie Seitenlänge B ein (in cm): "))

berechnungFlächeInhalt = längeA * längeB
berechnungUmfang = 2 * längeA + 2 * längeB

print(f"Die Fläche des Rechtecks beträgt: {berechnungFlächeInhalt:.2f} cm²")
print(f"Der Umfang des Rechtecks beträgt: {berechnungUmfang:.2f} cm")