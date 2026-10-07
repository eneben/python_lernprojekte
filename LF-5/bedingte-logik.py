# Funktion zum Noten Berechnen

def note_berechnen(punkte):
    if punkte < 0:
        raise ValueError("Punkte können nicht negativ sein.")
    elif punkte >= 90:
        return "1: Sehr gut"
    elif punkte >= 75:
        return "2: Gut"
    elif punkte >= 60:
        return "3: Befriedigend"
    elif punkte >= 50:
        return "4: Ausreichend"
    else:
        return "Nicht bestanden"

# punkte = int(input("Bitte geben Sie Ihre Punkte ein: "))

# print("Die Note ist: ", note_berechnen(punkte))

assert note_berechnen(95) == "1: Sehr gut" # Normal
assert note_berechnen(90) == "1: Sehr gut" # Grenze
assert note_berechnen(89) == "2: Gut" # knapp
assert note_berechnen(0) == "Nicht bestanden"

print("Alle Tests erfolgreich.")