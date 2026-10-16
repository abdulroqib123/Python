a = int(input("A: "))
b = int(input("B: "))


if a == 0:
    print("a darf nicht 0 sein!")
elif b == 0:
    print("b darf nicht 0 sein!")
else:
    lösung = -b / a
    print(f"Lösung {lösung}")