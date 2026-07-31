import os

task_list = []
def neuesdic():
	task_list.append({"text": "", "erledigt": False})

def headline(punkt):
	return "\n" + menü_optionen[punkt - 1] + "\n (back um zum Hauptmenü zurückzukehren)"

def hauptmenü():
	print("Hauptmenü ≣\n")
	i = 0
	for punkt in menü_optionen:
		i += 1
		print(f"{i}. {punkt} \n")

def clear():
	os.system("clear")
	
def programm_ende():
	print("\nProgramm beendet")
	quit()

def menü_abfrage():
	print("\n") 
	auswahl = input("Auswahl: ")
	return auswahl

def emoji(aufgb):
    if aufgb["erledigt"] == True:
            return("✅")
    else:
        return("❌")	
	
def menü_task_add():
	print(headline(1))
	while True:
		neue_task = input("Neue Aufgabe: ")
		if neue_task == "back":
				clear()
				return
		else:
			länge = len(task_list)
			neuesdic()
			task_list[länge]["text"] = neue_task
			clear()
			print("\nTask hinzugefügt ✅\n")
		
def show_tasks():
	for i, task in enumerate(task_list, start=1):
		print(str(i) +"." + task["text"]+": " + emoji(task))
		
def zurück_hauptmenü():
	while True:
		zurück = input("")
		if zurück == "back":
			clear()
			return
			
def menü_task_show():
	print(headline(2))
	print("\n")
	show_tasks()
	zurück_hauptmenü()
	return

def menü_task_completed():
	clear()
	print(headline(3))
	show_tasks()
	while True:
		eingabe = input("Wähle die erledigte task aus, mit zb. 1, 3...: ")
		if eingabe == "back":
			clear
			return
		try:
			eingabe = int(eingabe)
			if eingabe <= len(task_list):
				task_list[eingabe -1]["erledigt"] = True
				clear
				print(headline(3))
				show_tasks()
			else:
				print("Du musst eine Zahl angeben die zu einer task gehört.") 
		except:
			print("Du musst die Task mit einer Ganzzahl auswählen")



def menü_task_deleted():
	print(headline(4))
	show_tasks()
	while True:
		deleted_task = input("Wähle die task zum löschen aus, zb. 1, 3...: ")
		if deleted_task == "back":
			clear()
			return
		else:
			try:
				deleted_task = int(deleted_task)
				task_list.pop(deleted_task - 1)
				clear()
				print(f"Die {deleted_task}. Aufgabe wurde gelöscht✅")
				print(headline(4))
				show_tasks()
			except:
				clear()
				print("Du musst die zu löschende Task mit einer Zahl auswählen\n")
				print(headline(4))
				show_tasks()


	
menü_optionen = ["Aufgabe hinzufügen", "Alle Aufgaben anzeigen", "Aufgabe als erledigt makieren", "Aufgabe löschen", "Programm beenden"]



def hauptmenü_active():
	while True:
		hauptmenü()
		auswahl = menü_abfrage()
	
		if auswahl == "1":
			clear()
			menü_task_add()
		elif auswahl == "2":
			clear()
			menü_task_show()
		elif auswahl == "3":
			clear()
			menü_task_completed()
		elif auswahl == "4":
			clear()
			menü_task_deleted()
		elif auswahl == "5":
			clear()
			programm_ende()
		else:
			clear()

clear
hauptmenü_active()