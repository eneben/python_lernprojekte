# Praxisaufgabe · Der Notenrechner
# Drei kleine Funktionen, die zusammenarbeiten.


# Schritt 1
def durchschnitt(noten: list) -> float:
    if not noten:
        raise ValueError("Die Notenliste darf nicht leer sein.")
    for note in noten:
        if note > 6 or note < 1:
            raise ValueError("Die Note muss eine Zahl zwischen 1 und 6 sein.")
    return round(sum(noten) / len(noten),1)

assert durchschnitt([1, 2, 3]) == 2.0
assert durchschnitt([6]) == 6.0

try:
    durchschnitt([7, 2, 5])
except ValueError:
    pass
else:
    assert False, "Es hätte ein ValueError auftreten müssen."

print("Durchschnitt-Tests erfolgreich durchlaufen.")


# Schritt 2
def in_worten(note: int) -> str:
    if note == 1:
        return "sehr gut"
    elif note == 2:
        return "gut"
    elif note == 3:
        return "befriedigend"
    elif note == 4:
        return "ausreichend"
    elif note == 5:
        return "mangelhaft"
    elif note == 6:
        return "ungenügend"
    else:
        raise ValueError("Die Note muss zwischen 1 und 6 liegen.")


assert in_worten(3) == "befriedigend"
assert in_worten(1) == "sehr gut"

try:
    in_worten(0)
except ValueError:
    pass
else:
    assert False, "Es hätte ein ValueError auftreten müssen."

print("In-Worten-Tests erfolgreich durchlaufen.")


# Schritt 3
def bestanden(noten: list) -> bool:
    if durchschnitt(noten) <= 4.0:
        return True
    else:
        return False
    

assert bestanden([1, 2.2, 3]) == True
assert bestanden([4.0, 4]) == True
assert bestanden([4, 5]) == False

print("Bestanden-Tests erfolgreich durchlaufen.")


# Schritt 4: Ausgabe und Tests
bsp_noten = [2, 3, 1, 4, 2]

print("Durchschnitt: ", durchschnitt(bsp_noten))
print("Erste Note in Worten: ", in_worten(bsp_noten[0]))
print("Bestanden: ", bestanden(bsp_noten))


# Zusatz: Durchschnitt mit Nachkommastellen

def durchschnitt_mit_nachkommastellen_mit_zahlergebnis(noten: list, stellen: int = 1) -> float:
    if not noten:
        raise ValueError("Die Notenliste darf nicht leer sein.")
    for note in noten:
        if note > 6 or note < 1:
            raise ValueError("Die Note muss eine Zahl zwischen 1 und 6 sein.")
    durchschnitt = sum(noten) / len(noten)
    return round(durchschnitt,stellen)

def durchschnitt_mit_nachkommastellen_mit_textergebnis(noten: list, stellen: int = 1) -> str:
    if not noten:
        raise ValueError("Die Notenliste darf nicht leer sein.")
    for note in noten:
        if note > 6 or note < 1:
            raise ValueError("Die Note muss eine Zahl zwischen 1 und 6 sein.")
    durchschnitt = sum(noten) / len(noten)
    return f"{durchschnitt:.{stellen}f}"

