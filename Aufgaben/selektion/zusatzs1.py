"""
#Aufgabe 1
name = input("Name eingeben: ")
alter = int(input("Alter eingeben: "))

if alter < 16:
    print(f"{name} ist {alter}")
elif alter >= 16 or alter <= 17:
    print(f"{name} ist {alter}")
else:
    print(f"{name} ist {alter}")
    """

"""
#Aufgabe 2
wert = int(input("Gib dein Einkaufswert ein: "))

rabatt5 = wert * 0.05
rabatt10 = wert * 0.1

if wert < 50:
    print(f"Ursprünglichen Preis: {wert}")
    print(f"Preis nach Rabatt: {wert}")
elif wert >= 50 and wert < 100:
    print(f"Ursprünglichen Preis: {wert}")
    print(f"Preis nach Rabatt: {wert - rabatt5}")
else:
    print(f"Ursprünglichen Preis: {wert}")
    print(f"Preis nach Rabatt: {wert - rabatt10}")
"""
"""
#Aufgabe 3
temp = int(input("Gib die Temparatur ein: "))

if temp < 5:
    print("Zieh eine warme Jacke an.")
elif temp >= 5 and temp <= 15:
    print("Eine Jacke ist sinnvoll")
elif temp >= 16 and temp <= 25:
    print("Das Wetter ist angenehm")
else:
    print("Es ist ziemlich warm ")
"""
"""
#Aufgabe 4
bPass = input("GIb deine Password ein: ")
bName = input("Gib deine Benutzername ein: ")

passwort = "Jakultabi326@+#"
benutzername = "drakj"

if bPass == passwort and bName == benutzername:
    print("Logging in...")
else:
    print("Password ist falsch oder der Benutzername exsitiert nicht.")
"""
"""
#Aufgabe 5
bWert = int(input("Gib deine Bestellwert ein: "))
lLand = input("Gib deine Lieferland ein: ")

if bWert < 30 and lLand == "Deutschland":
    versand = 5
    gesamt = bWert + versand
    print(f"Gesamtpreis: {gesamt}")
elif bWert >= 30 and lLand == "Deutschland":
    versand = 0
    gesamt = bWert + versand
    print(f"Gesamtpreis: {gesamt}")
elif bWert < 50 and lLand != "Deutschland":
        versand = 10
        gesamt = bWert + versand
        print(f"Gesamtpreis: {gesamt}")
else:
    versand = 5
    gesamt = bWert + versand
    print(f"Gesamtpreis: {gesamt}")
"""

"""
#Aufgabe 6
alter = int(input("GIb deine Alter ein: "))
wunschVorstellung = input("Gib deine gewünschte Vorstellung ein (normal oder abend): ")
schulerodernicht = input("Bist du Schüler (ja oder nein): ")

grundpreis = 12
preis = grundpreis

if alter < 16:
    preis = grundpreis - 4
    print(f"Tiketpreis: {preis}")
elif schulerodernicht == "ja":
    preis = grundpreis - 2
    print(f"Tiketpreis: {preis}")
elif wunschVorstellung == "abend":
    preis = grundpreis + 3
    print(f"Tiketpreis: {preis}")
elif preis < 4:
    preis += 1
    print(f"Tiketpreis: {preis}")
else:
    print("Rechnung nicht möglich")

"""

#Aufgabe 7
dVolument = int(input("Gib wie viele Datenvolumen du möchtest: "))
minTel = int(input("Wie viel Minuten Telefonierst du ungefähr: "))

basicDVolumen = 5
basicMinTel = 100

standardDVolumen = 20
standardMinTel = 500

premiumDVolumen = 200
premiumMinTel = 0

