notizen = []

def notiz_hinzufuegen(text):
    notizen.append(text)

def notizen_anzeigen(notizen):
    if not notizen:
        print("Keine Notizen")
    for nummer, notiz in enumerate(notizen, start=1):
        print(f"{nummer}: {notiz}")

def notiz_löschen(nummer):
    if 0 <= nummer < len(notizen):
        notizen.pop(nummer)
    else:
        print("Diese Notiz existiert nicht.")

while True:
    wahl = input("Was willst du machen? Wähle 1, 2, 3 oder 0 und bestätige mit Enter. \n 1 = Notiz hinzufügen | 2 = Notizen anzeigen | 3 = Notiz löschen | 0 = Ende \n")
    match wahl:
        case "1":
            text = input("Füge hier eine Notiz hinzu: ")
            notiz_hinzufuegen(text)
        case "2":
            notizen_anzeigen(notizen)
        case "3":
            nummer = int(input("Welche Notiz möchtest du löschen? Gib die Nummer an.")) - 1
            notiz_löschen(nummer)
        case "0":
            break
        case _:
            print("Ungültige Auswahl.")
