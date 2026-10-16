"""
gewinnA = 40
gewinnB = 30

m1FeurA = 2
m1FeurB = 1
m1ProduktionsZeit = 100

m2FeurA = 1
m2FeurB = 2
m2ProduktionsZeit = 80


m1ProductionsMengeA = m1ProduktionsZeit / m1FeurA
m1ProductionsMengeB = m1ProduktionsZeit / m1FeurB
print("Machine 1 produktionsmenge für product A", m1ProductionsMengeA)
print("Machine 1 produktionsmenge für product B", m1ProductionsMengeB)

print("------------------------------------------------------------------------")

m2ProductionsMengeA = m2ProduktionsZeit / m2FeurA
m2ProductionsMengeB = m2ProduktionsZeit / m2FeurB
print("Machine 2 produktionsmenge für product A", m2ProductionsMengeA)
print("Machine 2 produktionsmenge für product B", m2ProductionsMengeB)

print("------------------------------------------------------------------------")

m1MaxGewinnA = m1ProductionsMengeA * gewinnA
m1MaxGewinnB = m1ProductionsMengeB * gewinnB
print("Machine 1 max Gewinn für product A", m1MaxGewinnA)
print("Machine 1 produktionsmenge für product B", m1MaxGewinnB)

print("------------------------------------------------------------------------")

m2MaxGewinnA = m2ProductionsMengeA * gewinnA
m2MaxGewinnB = m2ProductionsMengeB * gewinnB
print("Machine 2 max Gewinn für product A", m2MaxGewinnA)
print("Machine 2 produktionsmenge für product B", m2MaxGewinnB)

"""


# AUFAGBE 2
gewinnT = 70
stundenProT = 2
kgHolzProT = 4

gewinnS = 40
stundenProS = 3
kgHolzProS = 2

verfügbarHolz = 120
verfügbarStunden = 100

anzahlMaxTische = verfügbarHolz / kgHolzProT
maxStundenTische = verfügbarStunden / stundenProT

anzahlMaxStuhle = verfügbarHolz / kgHolzProS
maxStundenStuhle = verfügbarStunden / stundenProS

holz = kgHolzProT * anzahlMaxTische + kgHolzProS * maxStundenStuhle <= verfügbarHolz
stunden = stundenProT * anzahlMaxTische + stundenProS * anzahlMaxStuhle <= verfügbarStunden

minTische = anzahlMaxTische >= 10

maxGewinn = gewinnT * anzahlMaxTische + gewinnS * anzahlMaxStuhle

print("Max Gewinn für Tiche: ", maxGewinn)
