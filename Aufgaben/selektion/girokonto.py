kontoDurchsnitt = int(input("Gib die durchscnittliche Kontostand ein: "))
zinssatz = 0.5

if kontoDurchsnitt >= 2000:
    zinsen = kontoDurchsnitt * zinssatz / 100
    print(f"Die Zinsen betragen: {zinsen}")
else: 
    print(f"Die Zinsen betragen: 0")