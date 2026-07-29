import os

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
	
def menü_task_add():
	print(headline(1))
	while True:
		neue_task = input("Neue Aufgabe: ")
		if neue_task == "back":
				clear()
				return
		else:
			task_list.append(neue_task)
			clear()
			print("\nTask hinzugefügt ✅\n")
		
def show_tasks():
	i = 0
	for task in task_list:
		i += 1
		print(f"{i}. {task}")
		
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

#def menü_task_completed():
#	clear()
#	show_tasks()
#	while True:
#		break


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

def headline(punkt):
	return "\n" + menü_optionen[punkt - 1] + "\n (back um zum Hauptmenü zurückzukehren)"
	
menü_optionen = ["Aufgabe hinzufügen", "Alle Aufgaben anzeigen", "Aufgabe als erledigt makieren", "Aufgabe löschen", "Programm beenden"]

task_list = []
#for task in task_list:
#	task_list.join("❌")

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
			#menü_task_completed()
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