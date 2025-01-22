import random

def din_attack():
    random_chans = random.randint(0, 100)
    random_crit_chans = random.randint(0, 100)

    # En loop som kollar ifall ditt svar finns i en lista
    while True:
        ditt_val = input(f"Vilken attack vill du välja?\n\n[Slag] - statistik \n-------------------------\nChans att träffa: {slag.chans}%\nSkada: {slag.skada}\nKritiskskada: {slag.crit_skada * slag.skada}\n-------------------------\n\n[Spark] - statistik\n-------------------------\nChans att träffa: {spark.chans}%\nSkada: {spark.skada}\nKritiskskada: {spark.crit_skada * spark.skada}\n-------------------------\nSVAR: \n\n").lower()
        giltig_attack = None

        for att in attacks:
            if att.namn.lower() == ditt_val.lower():
                giltig_attack = att  
                break

        if giltig_attack:
            attack_namn = giltig_attack.namn
            attack_skada = giltig_attack.skada
            attack_chans = giltig_attack.chans
            attack_crit_skada = giltig_attack.crit_skada
            attack_crit_chans = giltig_attack.crit_chans
            break

        else:
            print("Du valde en ogiltig attack. Försök igen.\n")

    # Kollar ifall du har prickat och gör kritisk skada
    if random_chans <= attack_chans:
        if random_crit_chans <= attack_crit_chans:
            print(f"Du valde {attack_namn} och gör {attack_skada * attack_crit_skada} kritisk skada")
            fiende.hälsa -= attack_skada * attack_crit_skada

        elif random_crit_chans > attack_crit_chans:
            print(f"Du valde {attack_namn} och gör {attack_skada} skada")
            fiende.hälsa -= attack_skada

    elif random_chans > attack_chans:
        print(f"Du valde {attack_namn} och missade")