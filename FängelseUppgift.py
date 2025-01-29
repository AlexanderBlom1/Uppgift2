import random

class Rum:
    def __init__(self, namn, beskrivning):
        self.namn = namn
        self.beskrivning = beskrivning
        self.val_rum = {}
        self.val_föremål = {}
        self.val_sök = {}
        self.har_vakt = False

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

def strid(din_hälsa, fiende_hälsa):
    while din_hälsa > 0 and fiende_hälsa > 0:
        print("\n" + "="*50)
        print_colored(f"Din hälsa: {din_hälsa}", "1;32")
        print_colored(f"Vaktens hälsa: {fiende_hälsa}", "1;31")
        print_colored("\nVad vill du göra?", "1;33")
        print_colored("1. Attackera", "0;33")
        print_colored("2. Försök fly", "0;33")
        
        val = input("\nVälj ett alternativ: ")
        
        if val == "1":
            skada = random.randint(1, 6)
            fiende_skada = random.randint(1, 4)
            
            fiende_hälsa -= skada
            print_colored(f"\nDu gör {skada} skada på vakten!", "1;32")
            
            if fiende_hälsa <= 0:
                print_colored("\nDu besegrade vakten!", "1;32")
                return True
                
            din_hälsa -= fiende_skada
            print_colored(f"Vakten gör {fiende_skada} skada på dig!", "1;31")
            
            if din_hälsa <= 0:
                print_colored("\nDu förlorade striden...", "1;31")
                return False
                
        elif val == "2":
            if random.random() < 0.3:
                print_colored("\nDu lyckades fly!", "1;32")
                return None
            else:
                fiende_skada = random.randint(1, 4)
                din_hälsa -= fiende_skada
                print_colored("\nDu misslyckades med att fly!", "1;31")
                print_colored(f"Vakten gör {fiende_skada} skada på dig!", "1;31")
                
        else:
            print_colored("Ogiltigt val.", "1;31")


start_rum = Rum("Start", "Du är i en  cell. Dörren är låst.")
korridor = Rum("Korridor", "En lång och smal korridor.")
vakt_rum = Rum("Vaktrum", "Du ser en vakt. Han ser arg ut och är redo att slåss!")
korridor_2 = Rum("Korridor 2", "Du fortsätter utifrån vaktrummet till ännu en korridor.")
slut_rum = Rum("slutet", "Du har klarat av spelet")

vakt_rum.har_vakt = True

nyckel = Föremål("Nyckel", "En rostig nyckel som kanske öppnar dörren.")
paper = Föremål("papper", "En bit papper med en kod på")


start_rum.lägg_till_sök_val("kolla runt i rummet")

korridor.lägg_till_förflyttnings_val("gå till vaktrum", vakt_rum)
korridor.lägg_till_förflyttnings_val("gå tillbaka", start_rum)

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
    
    if not aktuellt_rum.har_vakt:
        for val in aktuellt_rum.val_rum:
            print_colored(f"- {val}", "0;33")
        for val in aktuellt_rum.val_föremål:
            print_colored(f"- {val}", "0;33")
        for sök in aktuellt_rum.val_sök:
            print_colored(f"- {sök}", "0;33")
    else:
        print_colored("- slåss med vakt", "0;33")
    
    print_colored("- meny (återgå till huvudmenyn)", "0;33")
    return input("\nVad vill du göra? \n")

def spara_variabler():
    data = {
        "current_room": aktuellt_rum.namn,
        "has_key": har_nyckel,
        "room_searched": "kolla runt i rummet" not in start_rum.val_sök,
        "guard_defeated": not vakt_rum.har_vakt,
        "door_unlocked": "öppna dörr" in start_rum.val_rum
    }
    
   
    save_text = "\n".join([
        f"Aktuellt rum: {data['current_room']}",
        f"Har nyckel: {data['has_key']}",
        f"Rum undersökt: {data['room_searched']}",
        f"Vakt besegrad: {data['guard_defeated']}",
        f"Dörr upplåst: {data['door_unlocked']}"
    ])
    
    with open("storage.txt", "w", encoding='utf-8') as fil:
        fil.write(save_text)
    print_colored("Spelet har sparats!", "1;32")
    
def ladda_variabler():
    try:
        with open("storage.txt", "r", encoding='utf-8') as fil:
            lines = fil.readlines()
            data = {}
            
            for line in lines:
                key, value = line.strip().split(": ", 1)
                
              
                if key == "Aktuellt rum":
                    data[key] = value
                else:
                    data[key] = value == "True"
            
        rum_mappning = {
            "Start": start_rum,
            "Korridor": korridor,
            "Vaktrum": vakt_rum,
            "Korridor 2": korridor_2,
            "slutet": slut_rum
        }
        
        laddat_rum = rum_mappning[data["Aktuellt rum"]]
        har_kollat = data["Rum undersökt"]
        vakt_rum.har_vakt = not data["Vakt besegrad"]
        dörr_öppen = data["Dörr upplåst"]
        
        
        if not vakt_rum.har_vakt:
            vakt_rum.lägg_till_förflyttnings_val("gå till korridor", korridor_2)
            vakt_rum.lägg_till_förflyttnings_val("gå tillbaka", korridor)
            vakt_rum.beskrivning = "Vaktrummet är tomt. Vakten ligger medvetslös på golvet."
        
        
        start_rum.val_sök.clear()
        start_rum.val_föremål.clear()
        start_rum.val_rum.clear()
        
        if har_kollat and not data["Har nyckel"]:
            start_rum.lägg_till_rum_val("ta nyckel", nyckel.namn_föremål)
        elif not har_kollat:
            start_rum.lägg_till_sök_val("kolla runt i rummet")
            
        if dörr_öppen:
            start_rum.lägg_till_förflyttnings_val("öppna dörr", korridor)
                
        return laddat_rum, data["Har nyckel"]
    except Exception as e:
        print_colored(f"Kunde inte ladda sparning. Fel: {str(e)}", "1;31")
        return start_rum, False

Meny = True
Spel = False
aktuellt_rum = start_rum
har_nyckel = False

din_hälsa = 20
fiende_hälsa = 10

while True:
    while Meny:
        meny_val = visa_huvudmeny()
        
        if meny_val == "1":
            Meny = False
            Spel = True
        elif meny_val == "2":
            while True:
                print("\n" + "="*50)
                print_colored("1. Spara", "1;32")
                print_colored("2. Ladda", "1;32")
                print_colored("3. Återgå till huvudmeny", "1;32")
                
                val = input("\nVälj ett alternativ: ")
                if val == "1":
                    spara_variabler()
                elif val == "2":
                    loaded_rum, loaded_nyckel = ladda_variabler()
                    aktuellt_rum = loaded_rum
                    har_nyckel = loaded_nyckel
                    print_colored("Spelet har laddats!", "1;32")
                elif val == "3":
                    break
                else:
                    print_colored("Ogiltigt val.", "1;31")

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

        elif spel_val == "slåss med vakt" and aktuellt_rum.har_vakt:
            strid_resultat = strid(din_hälsa, fiende_hälsa)
            if strid_resultat == True:
                aktuellt_rum.har_vakt = False
                aktuellt_rum.beskrivning = "Vaktrummet är tomt. Vakten ligger medvetslös på golvet."
                aktuellt_rum.lägg_till_förflyttnings_val("gå till korridor", korridor_2)
                aktuellt_rum.lägg_till_förflyttnings_val("gå tillbaka", korridor)
            elif strid_resultat == False:
                print_colored("Du förlorade striden och vaknar upp i din cell...", "1;31")
                aktuellt_rum = start_rum
                din_hälsa = 20

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