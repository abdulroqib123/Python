spannung = float(input("Spannung (Volt): "))
strom = float(input("Strom (Ampere): "))

widerstand = spannung / strom
leistung = spannung * strom

print(f"Gesamtwiderstand: {widerstand:.2f} Ohm")
print(f"Die Leistung: {leistung:.2f} Watt")
