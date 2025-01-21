class Rum:
    def __init__(self, namn, beskrivning):
        self.namn = namn
        self.beskrivning = beskrivning
        self.val_rum = {}  # Lista för förflyt val
        self.val_föremål = {}
        self.val_sök = {}

    def lägg_till_förflyttnings_val(self, val_namn, nästa_rum):
        self.val_rum[val_namn] = nästa_rum
    
    def lägg_till_rum_val(self, val_namn, föremål):
        self.val_föremål[val_namn] = föremål

    def lägg_till_sök_val(self, val_namn):
        self.val_sök[val_namn] = val_namn

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
paper = Föremål("papper", "En bit papper med en kod på")

# Lägg till nyckel till start rummet
start_rum.lägg_till_sök_val("kolla runt i rummet")

# korrdior förflyt val
korridor.lägg_till_förflyttnings_val("gå till vaktrum", vakt_rum)
korridor.lägg_till_förflyttnings_val("gå tillbaka", start_rum)

# vaktrum förflyt val
vakt_rum.lägg_till_förflyttnings_val("gå till korridor", korridor_2)
vakt_rum.lägg_till_förflyttnings_val("gå tillbaka", korridor)

# korridor 2 förflyt val
korridor_2.lägg_till_förflyttnings_val("gå tillbaka", vakt_rum)
korridor_2.lägg_till_förflyttnings_val("gå ut", slut_rum)

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def visa_huvudmeny():
    print("\n" + "="*50)
    print_colored("1. Spela", "1;32")
    print_colored("2. Inställningar", "1;32")
    print_colored("3. Avsluta", "1;32")
    return input("\nVälj ett alternativ: \n")

def visa_spel_val(aktuellt_rum):
    print("\n" + "="*50)
    print_colored(f"Du är i: {aktuellt_rum.namn}", "1;34")
    print_colored(aktuellt_rum.beskrivning, "0;37")
    print_colored("Dina val:", "1;32")
    
    for val in aktuellt_rum.val_rum:
        print_colored(f"- {val}", "0;33")
    for val in aktuellt_rum.val_föremål:
        print_colored(f"- {val}", "0;33")
    for sök in aktuellt_rum.val_sök:
        print_colored(f"- {sök}", "0;33")
    
    print_colored("- meny (återgå till huvudmenyn)", "0;33")
    return input("\nVad vill du göra? \n")

def spara_variabler():
    return

# -------------------------Spel loop------------------------- #
Meny = True
Spel = False
aktuellt_rum = start_rum
har_nyckel = False

while True:
    while Meny:
        meny_val = visa_huvudmeny()
        
        if meny_val == "1":
            Meny = False
            Spel = True
        elif meny_val == "2":
            print_colored("Inställningar är inte tillgängliga just nu.", "1;31")
        elif meny_val == "3":
            print_colored("Avslutar spelet...", "1;31")
            exit()
        else:
            print_colored("Ogiltigt val. Försök igen.", "1;31")
    
    while Spel:
        spel_val = visa_spel_val(aktuellt_rum)
        
        if spel_val.lower() == "meny":
            Spel = False
            Meny = True
            break
            
        elif spel_val == "ta nyckel" and "ta nyckel" in aktuellt_rum.val_föremål:
            har_nyckel = True
            del aktuellt_rum.val_föremål["ta nyckel"]
            print_colored("Du tar upp nyckeln", "1;32")

            if "öppna dörr" not in aktuellt_rum.val_rum:
                aktuellt_rum.lägg_till_förflyttnings_val("öppna dörr", korridor)

        elif spel_val == "öppna dörr" and not har_nyckel:
            print_colored("Dörren är låst. Du behöver en nyckel.", "1;31")

        elif spel_val in aktuellt_rum.val_sök:
            del aktuellt_rum.val_sök[spel_val]
            start_rum.lägg_till_rum_val("ta nyckel", nyckel.namn_föremål)
            print_colored(f"Du hittar {nyckel.namn_föremål}", "1;32")

        else:
            nästa_rum = aktuellt_rum.gå_till(spel_val)
            if nästa_rum:
                aktuellt_rum = nästa_rum
            else:
                print_colored("Ogiltigt val. Försök igen.", "1;31")