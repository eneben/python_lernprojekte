# Praxisaufgabe · Wiederholung: Der Wochenbericht des IT-Supports
# Der Support exportiert die Bearbeitungszeiten der Tickets einer Woche (in Minuten)
# als eine einzige Textzeile. Daraus soll ein kurzer Wochenbericht entstehen.
# Die Lösung steht in praxisaufgabe_loesung.py.

roh = "45;120;15;200;30;95;10;150"

# Schritt 1: Datentypen und Variablen
def einlesen(text):
    if not text:
        return []
    text_teile = text.split(";")
    zeiten = []
    for text_teil in text_teile:
        zeiten.append(int(text_teil))
    return zeiten

zeiten = einlesen(roh)
assert einlesen("5;10") == [5, 10]
assert einlesen("") == []
print("Tests zu Funktion: einlesen durchgelaufen.")

# print(zeiten)

# Schritt 2: Bedingte Logik
def einstufen(minuten):
    if minuten < 0:
        raise ValueError("Falsche Eingabe, Dauer negativ.")
    elif minuten <= 30:
        return "schnell"
    elif minuten <= 120:
        return "normal"
    else:
        return "lang"

assert einstufen(30) == "schnell"
assert einstufen(31) == "normal"
assert einstufen(120) == "normal"
assert einstufen(121) == "lang"

try:
    einstufen(-7)
except ValueError:
    pass
else:
    assert False, "Es hätte ein ValueError auftreten müssen."

print("Tests zu Funktion: einstufen durchgelaufen.")


# Schritt 3: Listen und Schleifen
def zaehle_stufen(dauern):
    schnell = 0
    normal = 0
    lang = 0
    for dauer in dauern:
        stufe = einstufen(dauer)
        if stufe == "schnell":
            schnell += 1
        elif stufe == "normal":
            normal += 1
        else:
            lang += 1
    return [schnell, normal, lang]

# print(zaehle_stufen(zeiten))

assert zaehle_stufen([5, 17, 35, 300, 50, 6]) == [3, 2, 1]
assert zaehle_stufen([]) == [0,0,0]
print("Tests zu Funktion: zaehle_stufen durchgelaufen.")


def lange_tickets(dauern):
    lange_tickets = []
    for dauer in dauern:
        stufe = einstufen(dauer)
        if stufe == "lang":
            lange_tickets.append(dauer)
    return lange_tickets

# print(lange_tickets(zeiten))

assert lange_tickets([5, 17, 35, 300, 50, 6]) == [300]
assert lange_tickets([5, 17, 35, 50, 6]) == []
print("Tests zu Funktion: lange_tickets durchgelaufen.")


# Schritt 4: Funktionen
def durchschnitt(dauern):
    if not dauern:
        raise ValueError("Keine Dauern empfangen.")
    gesamtdauer = 0
    for dauer in dauern:
        gesamtdauer += dauer
    durchschnitt = round(gesamtdauer / len(dauern), 1)
    return durchschnitt

# print(durchschnitt(zeiten))
assert durchschnitt([5, 10, 15]) == 10

try:
    durchschnitt([])
except ValueError:
    pass
else:
    assert False, "Es hätte ein ValueError auftreten müssen."

print("Tests zu Funktion: durchschnitt durchgelaufen.")
print("Alle Tests bestanden.")
    
def bericht(dauern):
    print(dauern)
    print("Tickets: ", len(dauern))
    print("Durchschnitt: ", durchschnitt(dauern))
    print(f"schnell: {zaehle_stufen(dauern)[0]} | normal: {zaehle_stufen(dauern)[1]} | lang: {zaehle_stufen(dauern)[2]}")
    print("Lange Tickets: ", ", ".join(str(x) for x in (lange_tickets(dauern))))


# bericht(zeiten)


# Schritt 6: Nachtragen mit while
def eingaben_nachtragen():
    global zeiten
    eingabe_gewuenscht = True
    while eingabe_gewuenscht:
        eingabe = input("Bitte Minuten eingeben, andernfalls tippe 'ende': ")
        if eingabe == "ende":
            eingabe_gewuenscht = False
        else:
            try:
                if (int(eingabe)) > 0:
                    minuten = int(eingabe)
                    zeiten.append(minuten)
                else:
                    raise ValueError("Bitte gibt eine ganze positive Zahl ein.")
            except ValueError:
                print("Bitte gibt eine ganze positive Zahl ein.")
                
    bericht(zeiten)
            
        
eingaben_nachtragen()






#  dauern = einlesen(roh), dann in einer while-Schleife weitere Minuten abfragen.
#       "ende" beendet die Eingabe, ungültige Eingaben werden gemeldet und übersprungen.
#       Zum Schluss bericht(dauern) aufrufen.
