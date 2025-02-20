import random
# Klasser för att skapa rum och föremål
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


class Pussel:
    def __init__(self, fråga, svar):
        self.fråga = fråga
        self.svar = svar
        self.löst = False

    def kontrollera_svar(self, försök):
        return försök.lower() == self.svar.lower()

# Funktioner för att skapa rum och föremål
def initialize_rooms():
    # Existing connections
    start_rum.lägg_till_sök_val("kolla runt i rummet")
    
    # New room connections
    korridor.lägg_till_förflyttnings_val("gå tillbaka", start_rum)
    korridor.lägg_till_förflyttnings_val("utforska sidogång", fälla_rum)
    korridor.lägg_till_förflyttnings_val("fortsätt framåt", vakt_rum)
    
    fälla_rum.lägg_till_förflyttnings_val("gå tillbaka", korridor)
    fälla_rum.lägg_till_förflyttnings_val("försök korsa rummet", gåt_rum)
    
    gåt_rum.lägg_till_förflyttnings_val("gå tillbaka", fälla_rum)
    gåt_rum.lägg_till_förflyttnings_val("fortsätt framåt", labyrint_rum)
    
    labyrint_rum.lägg_till_förflyttnings_val("gå tillbaka", gåt_rum)
    labyrint_rum.lägg_till_förflyttnings_val("fortsätt framåt", korridor_2)
    
    vakt_rum.har_vakt = True
    
    korridor_2.lägg_till_förflyttnings_val("gå tillbaka", vakt_rum)
    korridor_2.lägg_till_förflyttnings_val("fortsätt mot friheten", slut_rum)


def strid(din_hälsa, fiende_hälsa): 
    while din_hälsa > 0 and fiende_hälsa > 0:
        print("\n" + "="*50)
        print_colored(f"Din livskraft: {din_hälsa} ❤️", "1;32")
        print_colored(f"Vaktens livskraft: {fiende_hälsa} 💔", "1;31")
        print_colored("\nTiden står stilla medan du överväger dina alternativ...", "1;33")
        print_colored("1. Attackera vakten med all din styrka", "0;33")
        print_colored("2. Försök smita förbi i skuggorna", "0;33")
        
        val = input("\nVad väljer du att göra, modige äventyrare? ")
        
        if val == "1":
            skada = random.randint(1, 6)
            fiende_skada = random.randint(1, 4)
            
            fiende_hälsa -= skada
            print_colored(f"\nMed åren av frustation bakom dig, landar din attack perfekt och gör {skada} i skada!", "1;32")
            
            if fiende_hälsa <= 0:
                print_colored("\nMed ett sista kraftfullt slag faller vakten till golvet. Segern är din, precis som i de gamla goda dagarna!", "1;32")
                return True
                
            din_hälsa -= fiende_skada
            print_colored(f"Vakten kontrar snabbt och träffar dig för {fiende_skada} i skada. Det påminner dig om boss-strider från förr...", "1;31")
            
            if din_hälsa <= 0:
                print_colored("\nMörkret omsluter dig medan du faller till golvet. Game Over...", "1;31")
                return False
                
        elif val == "2":
            if random.random() < 0.3:
                print_colored("\nMed samma smidighet som du en gång hade i gamla plattformsspel, lyckas du elegant smita förbi!", "1;32")
                return None
            else:
                fiende_skada = random.randint(1, 4)
                din_hälsa -= fiende_skada
                print_colored("\nVakten är snabbare än du räknat med - precis som de där omöjliga NPC:erna från förr!", "1;31")
                print_colored(f"Du snubblar och tar {fiende_skada} i skada!", "1;31")
                
        else:
            print_colored("*BLIP* Ogiltigt val. Försök igen...", "1;31")

# Rum och föremål med nostalgiska beskrivningar
start_rum = Rum("Fängelsecellen", 
    "Du befinner dig i en kall och fuktig cell, vars väggar bär spår av tidigare fångars försök till frihet. "
    "Den rostiga järndörren påminner dig om de otaliga dungeon-nivåerna du utforskat i din ungdom. "
    "Månskenet silar in genom ett litet gallerförsett fönster, precis som i de gamla äventyrsspelen.")

korridor = Rum("Den Dunkla Korridoren", 
    "Facklor på väggarna kastar flackande skuggor över den medeltida stenkorridoren. "
    "Luften är tung av damm och historia, och dina fotsteg ekar mot stenplattorna. "
    "Det påminner dig om de första 3D-spelen du spelade, där varje korridor kunde gömma både skatter och faror.")

vakt_rum = Rum("Vakternas Kvarter", 
    "En ensam vakt står vid sitt post, stor som en slutboss från ett klassiskt JRPG. "
    "Hans rustning blänker i fackelskenet och han har definitivt sett dig. "
    "Rummet är fyllt av halvtömda ölkrus och ett övergivet kortspel - en scen värdig vilket retro-RPG som helst.")

korridor_2 = Rum("Den Upplysta Korridoren", 
    "Denna korridor känns annorlunda. Dagsljus strilar in genom höga fönster och du kan känna en frisk bris. "
    "Frihetens doft påminner dig om när du äntligen klarade det där omöjliga spelet efter hundratals försök. "
    "Slutet känns nära nu...")

slut_rum = Rum("Frihetens Port", 
    "Du har nått den sista nivån! Framför dig öppnar sig världen i all sin prakt, "
    "precis som när eftertexterna rullade på dina favoritspel. "
    "Du har klarat det! Time to save and quit...")

fälla_rum = Rum("Den Förrädiska Hallen",
    "Ett rum fyllt med misstänksamma stenplattor på golvet. "
    "Din erfarenhet från plattformsspel säger dig att vissa av dessa måste vara fallgropar. "
    "På andra sidan rummet ser du en säker passage.")

gåt_rum = Rum("Visdomens Kammare",
    "En Ancient Android vaknar till liv när du kliver in. "
    "'För att passera måste du svara på min gåta', säger den mekaniska rösten. "
    "Du känner igen situationen från otaliga RPG-pussel.")

labyrint_rum = Rum("Den Förvirrande Labyrinten",
    "En komplex labyrint breder ut sig framför dig. "
    "Om bara du hade ett mini-map som i de gamla dungeons. "
    "Du måste lista ut den rätta vägen genom denna förvirrande konstruktion.")



nyckel = Föremål("Rostig Nyckel", 
    "En klassisk dungeon-nyckel som kunde varit hämtad direkt ur ett 90-tals äventyrsspel. "
    "Den känns tung och betydelsefull i din hand.")

paper = Föremål("Mystiskt Pergament", 
    "Ett gulnat pergament med en hemlig kod. Det kunde lika gärna varit lösenordet "
    "till nästa nivå i ett av dina gamla favoritspel.")

gåta = Pussel(
    "Jag har städer, men inga hus.\nJag har berg, men inga träd.\nJag har vatten, men ingen fisk.\nJag har vägar, men inga bilar.\nVad är jag?",
    "karta"
)

def hantera_fällor():
    print_colored("\nDu ser tre vägar framför dig:", "1;33")
    print_colored("1. Hoppa på de röda plattorna", "0;33")
    print_colored("2. Följ den gröna stigen", "0;33")
    print_colored("3. Balansera på de blå stenarna", "0;33")
    
    val = input("\nVilken väg väljer du? ")
    if val == "2":  # Den rätta vägen
        print_colored("\nMed åratals erfarenhet av plattformsspel väljer du instinktivt den rätta vägen!", "1;32")
        return True
    else:
        print_colored("\nGolvet ger vika under dina fötter och du faller tillbaka till din cell!", "1;31")
        return False

def navigera_labyrint():
    print_colored("\nDu står inför tre gångar:", "1;33")
    print_colored("1. Den mörka tunneln till vänster", "0;33")
    print_colored("2. Den upplysta passagen i mitten", "0;33")
    print_colored("3. Den mystiska korridoren till höger", "0;33")
    
    försök = 3
    while försök > 0:
        val = input(f"\nVilken väg väljer du? ({försök} försök kvar) ")
        if val == "3":  # Rätt väg
            print_colored("\nDin intuition från otaliga dungeon crawlers leder dig rätt!", "1;32")
            return True
        else:
            försök -= 1
            if försök > 0:
                print_colored("\nDu går vilse och hamnar tillbaka vid början...", "1;31")
            else:
                print_colored("\nUtmattad och förvirrad hittar du vägen tillbaka till din cell...", "1;31")
                return False

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def visa_huvudmeny():
    print("\n" + "="*50)
    print_colored("╔══════════════════════════════════╗", "1;34")
    print_colored("║        DUNGEON ESCAPE 1.0        ║", "1;34")
    print_colored("║   Ett retro-inspirerat äventyr   ║", "1;34")
    print_colored("╚══════════════════════════════════╝", "1;34")
    print_colored("1. Starta Nytt Äventyr", "1;32")
    print_colored("2. Spara/Ladda Spelet", "1;32")
    print_colored("3. Avsluta till DOS", "1;32")
    return input("\nVälj ditt öde (1-3): ")

# Funktion för att visa val i spelet
def visa_spel_val(aktuellt_rum):
    print("\n" + "="*50)
    print_colored(f"Plats: {aktuellt_rum.namn}", "1;34")
    print_colored(aktuellt_rum.beskrivning, "0;37")
    print_colored("\nTillgängliga kommandon:", "1;32")

    val_meny = []
    index = 1  # Index för att hålla koll på valen
#    Om rummet har en vakt, visa endast stridsval
    if aktuellt_rum.har_vakt:
        print_colored("1. Slåss med vakt", "0;33")
        val_meny.append("slåss med vakt")
    else:
        for val in aktuellt_rum.val_rum:
            print_colored(f"{index}. {val}", "0;33")
            val_meny.append(val)
            index += 1

        for val in aktuellt_rum.val_föremål:
            print_colored(f"{index}. {val}", "0;33")
            val_meny.append(val)
            index += 1

        for sök in aktuellt_rum.val_sök:
            print_colored(f"{index}. {sök}", "0;33")
            val_meny.append(sök)
            index += 1

    print_colored(f"{index}. Meny (spara/ladda spelet)", "0;33")
    val_meny.append("meny")
    # Användaren får välja ett alternativ
    try:
        val = int(input("\nVad är ditt nästa drag? "))
        if 1 <= val <= len(val_meny): # Om valet är giltigt
            return val_meny[val - 1]
        else:
            print_colored("Ogiltigt val. Försök igen.", "1;31")
            return visa_spel_val(aktuellt_rum)
    except ValueError: # Om användaren inte skriver en siffra
        print_colored("Ogiltigt val. Ange en siffra.", "1;31")
        return visa_spel_val(aktuellt_rum)

# Funktioner för att spara och ladda spelet
def spara_variabler():
    data = {
        
        "current_room": aktuellt_rum.namn,
        "has_key": har_nyckel,
        "room_searched": "kolla runt i rummet" not in start_rum.val_sök,
        "guard_defeated": not vakt_rum.har_vakt,
        "door_unlocked": "öppna dörr" in start_rum.val_rum
    }
    
    save_text = "\n".join([ # Skapar en sträng med variablerna
        f"Aktuellt rum: {data['current_room']}",
        f"Har nyckel: {data['has_key']}",
        f"Rum undersökt: {data['room_searched']}",
        f"Vakt besegrad: {data['guard_defeated']}",
        f"Dörr upplåst: {data['door_unlocked']}"
    ])
    
    with open("storage.txt", "w", encoding='utf-8') as fil:
        fil.write(save_text)
    print_colored("Spelet har sparats!", "1;32")
    
# Funktion för att ladda spelet
def ladda_variabler():
    try:
        with open("storage.txt", "r", encoding='utf-8') as fil:
            lines = fil.readlines()
            data = {}
            
            for line in lines: # Läser in variablerna från filen
                key, value = line.strip().split(": ", 1)
                
                if key == "Aktuellt rum": # Om det är aktuellt rum
                    data[key] = value
                else: # Om det är en boolean-variabel
                    data[key] = value == "True" 
            
        rum_mappning = { # Mappar rummen till variablerna
            "Fängelsecellen": start_rum,
            "Den Dunkla Korridoren": korridor,
            "Vakternas Kvarter": vakt_rum,
            "Den Upplysta Korridoren": korridor_2,
            "Frihetens Port": slut_rum
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

#
initialize_rooms()
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

        elif spel_val == "försök korsa rummet" and aktuellt_rum == fälla_rum:
            if hantera_fällor():
                aktuellt_rum = gåt_rum
            else:
                aktuellt_rum = start_rum
                
        elif spel_val == "fortsätt framåt" and aktuellt_rum == gåt_rum:
            print_colored("\n" + gåta.fråga, "1;33")
            svar = input("\nDitt svar: ")
            if gåta.kontrollera_svar(svar):
                print_colored("\nAndrouden nickar godkännande. 'Du har klarat provet!'", "1;32")
                aktuellt_rum = labyrint_rum
            else:
                print_colored("\n'Fel svar!' Androuden aktiverar en fälla och du faller tillbaka till din cell.", "1;31")
                aktuellt_rum = start_rum
                
        elif spel_val == "fortsätt framåt" and aktuellt_rum == labyrint_rum:
            if navigera_labyrint():
                aktuellt_rum = korridor_2
            else:
                aktuellt_rum = start_rum

        else:
            nästa_rum = aktuellt_rum.gå_till(spel_val)
            if nästa_rum:
                aktuellt_rum = nästa_rum
            else:
                print_colored("Ogiltigt val. Försök igen.", "1;31")