import random

secret = random.randint(0, 20)
guess = input("Zahl zwischen 0 und 20, du hast 5 Versuche: ")
trys = 5
while secret != int(guess) and trys > 1:
    trys -= 1   
    if int(guess) < secret:
        print("Größer als " + str(guess))
    elif int(guess) > secret:
        print("Kleiner als " + str(guess))
    if trys > 1:
        print("noch " + str(trys) + " Versuche")
    elif trys == 0: 
        print("Kein Versuch mehr übrig") 
    else:
        print(f"noch {trys} Versuch") 
    print("")

    guess = input("Zahl zwischen 0 und 20, noch" + str(trys) + "Versuche : ")

if int(guess) == secret:
    print("Herzlichen Glückwunsch!!")
else:
    print("Du hast verloren!")

print("Die Zahl war " + str(secret))
