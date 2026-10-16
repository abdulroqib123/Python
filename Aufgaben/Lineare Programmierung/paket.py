breite = float(input("Breite das Paketes (In cm): "))
hoehe = float(input("Höhe das Pakets (in cm): "))
tiefe = float(input("Tiefe das Pakets (in cm): "))

oberfläche = 2 * (breite * hoehe + tiefe * hoehe + tiefe * breite)
volumen = breite * tiefe * hoehe
schnur = (2 * breite + 2 * hoehe) + 15

geschenkPapieresKosten = oberfläche * 0.3
schnurKosten = schnur * 0.1

print("-------------------------------------------------------------")

print(f"Der Geschenkpapierverbrauch liegt bei: {oberfläche} cm²", )
print(f"Volumeninhalt liegt bei: {volumen} cm³")
print(f"Die Länge der Schnur beträgt: {schnur} cm")

print("-------------------------------------------------------------")

print(f"Die kosten des Geschenkpapieres liegen bei {geschenkPapieresKosten} Euro, die der schnur bei {schnurKosten} Euro")
print(f"Die Gesamtkosten liegen bei: {geschenkPapieresKosten + schnurKosten} Euro")
