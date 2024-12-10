

class Rum:
    def __init__(self, namn, beskrivning):
        self.namn = namn
        self.beskrivning = beskrivning
        self.val_rum = {}  # Lista för förflyt val
        self.val_föremål = {}

    def lägg_till_förflyttnings_val(self, val_namn, nästa_rum):
        self.val[val_namn] = nästa_rum
    
    def lägg_till_rum_val(self, val_namn, föremål):
        self.val[val_namn] = föremål

    def gå_till(self, val_namn):
        return self.val_rum.get(val_namn, None)
    

class Föremål:
    def __init__(self, namn_föremål, beskrivning_föremål, har):
        self.namn_föremål = namn_föremål
        self.beskrivning_föremål = beskrivning_föremål
        
    

# Variabler för varje rum [NAMN, BESKRIVNING]
start_rum = Rum("Start", "Du är i en mörk cell. Dörren är låst.")
korridor = Rum("Korridor", "En lång och smal korridor.")
vakt_rum = Rum("Vaktrum", "Du ser en vakt. Han verkar sova.")

# Variabler för varje val för respektive rum [VAL, RUM]

# start förflyt val
start_rum.lägg_till_förflyttnings_val("öppna dörr", korridor)




# korrdior förflyt val
korridor.lägg_till_förflyttnings_val("gå till vaktrum", vakt_rum)
korridor.lägg_till_förflyttnings_val("gå tillbaka", start_rum)

# vaktrum förflyt val
vakt_rum.lägg_till_förflyttnings_val("", vakt_rum)


# -------------------------Spel loop------------------------- #
aktuellt_rum = start_rum
while True:
    print(f"Du är i: {aktuellt_rum.namn}")
    print(aktuellt_rum.beskrivning)
    print("Dina val:")
    for val in aktuellt_rum.val_rum:
        print(f"- {val}")

    spel_val = input("Vad vill du göra? \n")
    nästa_rum = aktuellt_rum.gå_till(spel_val)
    if nästa_rum:
        aktuellt_rum = nästa_rum
    else:
        print("Ogiltigt val. Försök igen.")
# -------------------------Spel loop------------------------- #