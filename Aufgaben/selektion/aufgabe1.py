# Aufgabe 2
zahl = int(input("Gib eine Zahl ein: "))

if zahl % 2 == 0:
    print("Die gegebene Zahl ist gerade")
else:
    print("Die gegebene Zahl ist ungerade")
    
# Aufgabe 3
note = int(input("Gib eine Note ein: "))

if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
elif note == 4:
    print("Ausreichend")
elif note == 5:
    print("Mangelhaft")
elif note == 6:
    print("Ungenügend")
else:
    print("Gib bitte eine Note zwischen 1 und 6")

# Aufgabe 4
farbe = input("Gib eine Ampelfarbe ein: ")

if farbe == "rot":
    print("Stop")
elif farbe == "gelb":
    print("Achtung")
elif farbe == "grün":
    print("Los")
else:
    print("GIb bitte eine Ampelfarbe ein")

# Aufgabe 5
wert = int(input("Gib der Einkaufswert ein: "))

if wert > 100:
    endpreis = wert * 10 / 100
    print(f"Der Endpreis ist {wert - endpreis}")
else:
    print(f"Der Endpreis ist {wert}")

# Aufgabe 6
password = "gabikotelki@231+"
gegebenPass = input("Gib das Password ein: ")

if gegebenPass == password:
    print("Sie sind angemeldet")
else: 
    print("False Password")
