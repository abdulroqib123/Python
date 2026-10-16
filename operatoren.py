#AUFAGBE 1
a = int(input("Gib die erste Zahl ein: "))
b = int(input("Gib die zweite Zahl ein: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 2
brotchenPreis = 2
anzahlBrotchen = 4
print(f"Ich muss {brotchenPreis * anzahlBrotchen} Euro bezahlen, wenn ich {anzahlBrotchen} kaufe")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 3
miasGeld = 15
omasGeschenk = 5
print(f"Mia hat {miasGeld} Euro und sie bekommt noch {omasGeschenk} Euro von Oma. Deswegen hat sie {miasGeld + omasGeschenk}")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 4
anzahlBonbons = 20
anzahlKinder = 4
print(f"Weil es nur {anzahlBonbons} Bonbons gibt, bekommt jeder Kind {anzahlBonbons / anzahlKinder} Bonbons")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 5
anzahlBonbons = 17
anzahlKinder = 5
print(f"Wenn wir {anzahlBonbons} Bonbons zwischen {anzahlKinder} Kinder verteilen, bleibt noch {anzahlBonbons % anzahlKinder} Bonbons")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 6
timAlter = 14
leaAlter = 16
print(f"Tim ist älter als Lea {timAlter > leaAlter}")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 7
comuterspielKoste = 30
meinGeld = 35
print(f"Ich habe genug Geld, um das Spiel zu kaufen {meinGeld >= comuterspielKoste}")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 8
anzahlSchüler = 24
print(f"Der zahl ist gerade {anzahlSchüler % 2 == 0}")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 9
punkte = 100
erhaltetPunkte = 25
punkte += erhaltetPunkte
print(f"Neue punkte sind {punkte}")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 10
mindestAlter = 12
schauerAlter = 14
hatTicket = True
print(f"Die Person can das Film sehen {schauerAlter >= mindestAlter and hatTicket}")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#AUFGABE 11
pizzaStuck = 8
anzahlPerson = 3
gegessenStuckProPerson = 2
print(f"Wenn {anzahlPerson} essen jeweils {gegessenStuckProPerson} von eine {pizzaStuck} stücke Pizza, gibt es noch {pizzaStuck - anzahlPerson * gegessenStuckProPerson} stücke Pizza.")