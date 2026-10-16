längeA = float(input("BItte geben sie die Seitenlänge A ein (in cm): "))
längeB = float(input("BItte geben sie die Seitenlänge B ein (in cm): "))
höhe = float(input("BItte geben sie die Höhe ein (in cm): "))

berechnungFlächeInhalt = längeA * höhe
berechnungUmfang = 2 * längeA + 2 * längeB

print(f"Die Fläche des Parallelogram beträgt: {berechnungFlächeInhalt:.2f} cm²")
print(f"Der Umfang des Parallelogram beträgt: {berechnungUmfang:.2f} cm")