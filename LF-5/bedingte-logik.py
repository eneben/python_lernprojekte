# Funktion zum Noten Berechnen

def note_berechnen(punkte):
    if punkte >= 90:
        return "Sehr gut"
    elif punkte >= 75:
        return "Gut"
    elif punkte >= 60:
        return "Befriedigend"
    elif punkte >= 50:
        return "Ausreichend"
    else:
        return "Nicht bestanden"

punkte = int(input("Bitte geben Sie Ihre Punkte ein: "))

print("Die Note ist: ", note_berechnen(punkte))

