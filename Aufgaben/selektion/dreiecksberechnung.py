seiteA = float(input("Seite a: "))
seiteB = float(input("Seite b: "))
seiteC = float(input("Seite c: "))

if (seiteA + seiteB > seiteC) and (seiteA + seiteC > seiteB) and (seiteB + seiteC > seiteA):
    print("Das Dreieck ist konstruierbar!")
else:
    print("Das Dreieck ist nich konstruierbar!")