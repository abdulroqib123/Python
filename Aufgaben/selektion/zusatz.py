"""
alter = int(input("ALter: "))
buchungsklasse = input("Buchungsklasse(economy oder business): ")
anzahlGepäckstücke = int(input("Anzahl Gepäckstücke: "))
istMitglied = input("Bist du mitglied(ja oder nein): ")

economyPreis = 180
businessPreis = 420

economyIstUnter18 = economyPreis * 15 / 100
economyistMitglieder = economyPreis * 10 / 100

businessIstUnter18 = businessPreis * 15 / 100
businessistMitglieder = businessPreis * 10 / 100

gepäckKostenEconomy = (anzahlGepäckstücke - 1) * 35
gepäckKostenBusiness = (anzahlGepäckstücke - 2) * 35

gepäckKosten = 0
ticketPreis = 0

if buchungsklasse == "economy":
      ticketPreis = economyPreis

      if anzahlGepäckstücke > 1:
            gepäckKosten = gepäckKostenEconomy
      if istMitglied == "ja":
            ticketPreis = ticketPreis - economyistMitglieder
      if alter < 18:
            ticketPreis = ticketPreis - economyIstUnter18
else:
      ticketPreis = businessPreis

      if anzahlGepäckstücke > 2:
            gepäckKosten = gepäckKostenBusiness
      if istMitglied == "ja":
            ticketPreis = ticketPreis - businessistMitglieder
      if alter < 18:
            ticketPreis = ticketPreis - businessIstUnter18

print(f"Ticketpreis: {ticketPreis}")
print(f"Gepäckkosten: {gepäckKosten}")
print(f"Gesamtpreis: {ticketPreis + gepäckKosten}")
"""

alter = int(input("ALter: "))
klasse = input("Fahrzeugklasse (klein, mittel oder premium): ").lower()
mietdauer = int(input("Mietdauer (In Tagen): "))
istZusatz = input("Ist Zusatzversicherung gewünscht? (ja oder nein): ").lower()

kleinPreis = 35
mittelPreis = 55
premiumPreis = 90

kleinIstUnter25 = kleinPreis * mietdauer + 15 * mietdauer
mittelIstUnter25 = mittelPreis * mietdauer + 15 * mietdauer
premiumIstUnter25 = premiumPreis * mietdauer + 15 * mietdauer

kleinAb7 = kleinPreis * 15 / mietdauer
mittelAb7 = mittelPreis * 15 / mietdauer
premiumAb7 = premiumPreis * 15 / mietdauer

kleinZusatzKosten = kleinPreis * mietdauer + 8 * mietdauer
mittelZusatzKosten = mittelPreis * mietdauer + 8 * mietdauer
premiumZusatzKosten = premiumPreis * mietdauer + 8 * mietdauer

