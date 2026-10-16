sollstunden = int(input("Was sind ihre Sollstunden (Monat)?: "))
iststunden = int(input("Was sind ihre Iststunden (Monat)?: "))
stundenlohn = int(input("Was ist ihre Stundenlohn (Euro)?: "))


überstunden10 = sollstunden * 10 / 100
überstundenZuschlag25 = stundenlohn * 25 / 100
überstundenZuschlag30 = stundenlohn * 30 / 100

überstunden = iststunden - sollstunden

print (f"Sie haben in Monat {überstunden} überstunden gemacht")

if überstunden <= überstunden10:
    endeStundenlohn = überstunden * überstundenZuschlag25
    print(f"Sie bekommen {endeStundenlohn} Euro zusätzlich ausgezahlt")
    print(f"Ihre Bruttolohn betägt: {stundenlohn * sollstunden + endeStundenlohn}")
elif überstunden > überstunden10:
    endeStundenlohn = überstunden * überstundenZuschlag30
    print(f"Sie bekommen {endeStundenlohn} Euro zusätzlich ausgezahlt")
    print(f"Ihre Bruttolohn betägt: {stundenlohn * sollstunden + endeStundenlohn}")