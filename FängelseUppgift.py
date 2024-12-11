class Rum:
    def __init__(self, namn, beskrivning):
        self.namn = namn
        self.beskrivning = beskrivning
        self.val_rum = {}  # Lista för förflyt val
        self.val_föremål = {}

    def lägg_till_förflyttnings_val(self, val_namn, nästa_rum):
        self.val_rum[val_namn] = nästa_rum
    
    def lägg_till_rum_val(self, val_namn, föremål):
        self.val_föremål[val_namn] = föremål

    def gå_till(self, val_namn):
        return self.val_rum.get(val_namn, None)
    

class Föremål:
    def __init__(self, namn_föremål, beskrivning_föremål):
        self.namn_föremål = namn_föremål
        self.beskrivning_föremål = beskrivning_föremål
        
    

# Variabler för varje rum [NAMN, BESKRIVNING]
start_rum = Rum("Start", "Du är i en mörk cell. Dörren är låst.")
korridor = Rum("Korridor", "En lång och smal korridor.")
vakt_rum = Rum("Vaktrum", "Du ser en vakt. Han verkar sova.")
korridor_2 = Rum("Korridor 2", "Du fortsätter utifrån vaktrummet till ännu en korridor.")
slut_rum = Rum("slutet", "Du har klarat av spelet")

# Skapa nyckel föremål
nyckel = Föremål("Nyckel", "En rostig nyckel som kanske öppnar dörren.")

# Lägg till nyckel till start rummet
start_rum.lägg_till_rum_val("ta nyckel", nyckel)

# Variabler för varje val för respektive rum [VAL, RUM]


# start förflyt val
start_rum.lägg_till_förflyttnings_val("öppna dörr", korridor)

# korrdior förflyt val
korridor.lägg_till_förflyttnings_val("gå till vaktrum", vakt_rum)
korridor.lägg_till_förflyttnings_val("gå tillbaka", start_rum)

# vaktrum förflyt val
vakt_rum.lägg_till_förflyttnings_val("gå till korridor", korridor_2)
vakt_rum.lägg_till_förflyttnings_val("gå tillbaka", korridor)

# korridor 2 förflyt val
korridor_2.lägg_till_förflyttnings_val("gå tillbaka", vakt_rum)
korridor_2.lägg_till_förflyttnings_val("gå ut", slut_rum)

# -------------------------Spel loop------------------------- #
aktuellt_rum = start_rum
har_nyckel = False

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

while True:
    
    print("\n" + "="*50)
    print_colored(f"Du är i: {aktuellt_rum.namn}", "1;34")  # Blå text
    print_colored(aktuellt_rum.beskrivning, "0;37")  # Vit text
    print_colored("Dina val:", "1;32")  # Grön text
    for val in aktuellt_rum.val_rum:
        print_colored(f"- {val}", "0;33")  # Gul text
    for val in aktuellt_rum.val_föremål:
        print_colored(f"- {val}", "0;33")  # Gul text

    spel_val = input("\nVad vill du göra? \n")
    
    if spel_val == "ta nyckel" and "ta nyckel" in aktuellt_rum.val_föremål:
        har_nyckel = True
        del aktuellt_rum.val_föremål["ta nyckel"]
        print_colored("Du tog nyckeln.", "1;32")  # Grön text
    elif spel_val == "öppna dörr" and not har_nyckel:
        print_colored("Dörren är låst. Du behöver en nyckel.", "1;31")  # Röd text
    else:
        nästa_rum = aktuellt_rum.gå_till(spel_val)
        if nästa_rum:
            aktuellt_rum = nästa_rum
        else:
            print_colored("Ogiltigt val. Försök igen.", "1;31")  # Röd text
# -------------------------Spel loop------------------------- #