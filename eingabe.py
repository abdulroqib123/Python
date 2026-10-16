"""
print("Hallo freund. Willkommen zu unsere umfrage.")
print("Dammit wir dich besser kennenlernen, möchten wir dir ein paar Fragen stellen.")

print("Frage eins")
name = input("Wie heißt du? ")

print("Frage zwei")
wohnort = input("Wo wohnst du? ")

print("Frage drei")
lieblingsFarbe = input("Was ist dein Lieblingsfarbe? ")

print("Guten Morgen,", name, "!")
print("Schön, dass du aus", wohnort, "kommst")
print("Deine Lieblingsfarbe ist ", lieblingsFarbe)
print("------------------------------------------------------------------------------------------------")


#Zahlen mit int() einlesen
geld = int(input("Wie viel Geld hast du? "))
taschenGeldInZehnTage = geld + 10
print("Wenn du jeden Tag 10 Euro bekommst, wirst du in 10 Tage ", taschenGeldInZehnTage, " Euro haben")

äpfel = int(input("Wie viel Äpfel hast du? "))
äpfelMallZwei = äpfel * 2
print("Wenn ich dir noch", äpfel, " gebe, wirst du " + äpfelMallZwei + " haben")

alter = int(input("Wie alt bist du? "))
alter += 5
print("In 5 Jahre wirst du ", alter, " Jahre alt sein")
print("------------------------------------------------------------------------------------------------")

"""


#Mini-Projekt: Steckbrief
Name = input("Wie heißt du? ")
Alter = int(input("Wie alt bist du? "))
Hobby = input("Was ist dein Hobby? ")
Lieblingsfach = input("Wo wohst du? ")
Lieblingstier = input("Was ist dein Lieblingstier? ")
print("                                     ")
print("-----------Dein Steckbrief-----------")
print("                                     ")
print("Name: ", Name)
print("Alter: ", Alter)
print("Hobby: ", Hobby)
print("Lieblingsfach ", Lieblingsfach)
print("Lieblingstier ", Lieblingstier)
print("In fünf Jahren wirst du ", Alter + 5, " Jahre alt sein")