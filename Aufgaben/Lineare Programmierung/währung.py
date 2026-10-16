pfund = int(input("Wie viel Pfund hast du? "))
schilling = int(input("Wie viel Schilling hast du? "))
pence = int(input("Wie viel Pence hast du? "))

schilling = schilling + pence / 12
pfund = pfund + schilling / 20

euro = pfund * 1.83

print(euro)