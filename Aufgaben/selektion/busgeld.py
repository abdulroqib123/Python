inAuß = input("Innerorts/Außerorts: ").lower()
verstoß = int(input("Geschwindigkeit (in km/h): "))

strafe = 0
punkte = 0
fahrverbot = 0

match inAuß:
      case "innerorts":
            if verstoß <= 10:
                  strafe = 30
            elif verstoß >= 11 and verstoß <= 15:
                  strafe = 50
            elif verstoß >= 16 and verstoß <= 20:
                  strafe = 70
            elif verstoß >= 21 and verstoß <= 25:
                  strafe = 115
                  punkte = 1
            elif verstoß >= 26 and verstoß <= 30:
                  strafe = 180
                  punkte = 1
                  fahrverbot = 1
            elif verstoß >= 31 and verstoß <= 40:
                  strafe = 260
                  punkte = 2
                  fahrverbot = 1
            elif verstoß >= 41 and verstoß <= 50:
                  strafe = 400
                  punkte = 2
                  fahrverbot = 1
            elif verstoß >= 51 and verstoß <= 60:
                  strafe = 560
                  punkte = 2
                  fahrverbot = 2
            elif verstoß >= 61 and verstoß <= 70:
                  strafe = 700
                  punkte = 2
                  fahrverbot = 3
            else:
                  strafe = 800
                  punkte = 2
                  fahrverbot = 3
      case "außerorts":
            if verstoß <= 10:
                  strafe = 20
            elif verstoß >= 11 and verstoß <= 15:
                  strafe = 40
            elif verstoß >= 16 and verstoß <= 20:
                  strafe = 60
            elif verstoß >= 21 and verstoß <= 25:
                  strafe = 100
                  punkte = 1
            elif verstoß >= 26 and verstoß <= 30:
                  strafe = 150
                  punkte = 1
                  fahrverbot = 1
            elif verstoß >= 31 and verstoß <= 40:
                  strafe = 200
                  punkte = 1
                  fahrverbot = 1
            elif verstoß >= 41 and verstoß <= 50:
                  strafe = 320
                  punkte = 2
                  fahrverbot = 1
            elif verstoß >= 51 and verstoß <= 60:
                  strafe = 480
                  punkte = 2
                  fahrverbot = 1
            elif verstoß >= 61 and verstoß <= 70:
                  strafe = 600
                  punkte = 2
                  fahrverbot = 2
            else:
                  strafe = 700
                  punkte = 2
                  fahrverbot = 3


print(f"Strafe: {strafe}€")
print(f"Punkte: {punkte}")

if fahrverbot > 1:
      print(f"Fahrverbot: {fahrverbot} monate")
else:
      print(f"Fahrverbot: {fahrverbot} monat")
      