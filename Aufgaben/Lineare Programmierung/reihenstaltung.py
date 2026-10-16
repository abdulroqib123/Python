r1 = float(input("R1 (Ohm) eingeben: "))
r2 = float(input("R2 (Ohm) eingeben: "))
r3 = float(input("R3 (Ohm) eingeben: "))

spannung = float(input("Spannung (Volt) eingeben: "))

Rges = r1 + r2 + r3
Iges = spannung / Rges

print(f"Gesamtwiderstand: {Rges:.3f} Ohm")
print(f"Strom: {Iges:.3f} Ampere")