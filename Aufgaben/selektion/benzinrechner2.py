km = int(input("Kilometer: "))
verbrauch = int(input("Verbrauch: "))

if km == 0:
    print("Ihr Durchschnittsverbrauch liegt bei 0.00 1/100km")
else:
    durchscnitt = verbrauch / km * 100
    print(f"Ihr Durchschnittsverbrauch liegt bei {durchscnitt} 1/100km")
