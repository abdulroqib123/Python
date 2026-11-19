
zahl1 = int(input("Schreib eine Zahl: "))
zahl2 = int(input("Schreib eine andere zahl: "))

while True:
      grundrechenart = input("Welche Rechenart soll durchgefürt werden? (1-addieren/2-subtrahieren/3-dividieren/4-multiplizieren): ")
      match grundrechenart:
            case "1":
                  ergebnis = zahl1  + zahl2
                  print("Ergebnis: ", ergebnis)
                  break
            case "2":
                  ergebnis = zahl1  - zahl2
                  print("Ergebnis: ", ergebnis)
                  break
            case "3":
                  ergebnis = zahl1  * zahl2
                  print("Ergebnis: ", ergebnis)
                  break
            case "4":
                  ergebnis = zahl1  / zahl2
                  print("Ergebnis: ", ergebnis)
                  break
            case _:
                  print("Falsche Eingabe")
