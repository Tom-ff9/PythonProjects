import random

def auswertung(einsatz1, einsatz2):
    if einsatz1 == einsatz2:
        return "unentschieden"
    
    elif einsatz1 == "schere":
        if einsatz2 == "papier":
            return "verloren"
        elif einsatz2 == "stein":
            return "gewonnen"
        
    elif einsatz1 == "papier":
        if einsatz2 == "stein":
            return "verloren"
        elif einsatz2 == "schere":
            return "gewonnen"
        
    elif einsatz1 == "stein":
        if einsatz2 == "schere":
            return "verloren"
        elif einsatz2 == "papier":
            return "gewonnen"
        
wahlende = True

while wahlende:
    comp = random.choice(["schere", "stein", "papier"])
    player = input("Schere Stein oder Papier: ").strip().lower()

    while player not in ["schere", "stein", "papier"]:
        print("ungültige eingabe")
        player = input("Schere Stein oder Papier: ")
    print("Der Computer hatte:" + comp)
    print("Du hast " + auswertung(comp, player))
    print("")
    
    while True:
        try:
            wahl = int(input("1): spielen\n2): beenden\nAuswahl:"))
            if wahl == 1:
                break
            elif wahl == 2:
                wahlende = False
                break
            else:
                print("Gebe 1 oder 2 ein")
        except ValueError:
            print("Bitte Zahl eingeben")
