# Praxisaufgabe · Einkaufsliste für das Teamfrühstück

# Schritt 1: Liste anlegen und ausgeben

einkaufsliste = ["Brötchen", "Butter", "Käse"]
print(einkaufsliste)

# Schritt 2: Liste verändern

einkaufsliste.append("Marmelade")
einkaufsliste.remove("Butter")
print("Anzahl Artikel: ", len(einkaufsliste))

# Schritt 3: Nummerierte Liste

def nummerierte_liste(liste):
    for i, item in enumerate(liste, start=1):
        print(i, ": ", item)

nummerierte_liste(einkaufsliste)

# Schritt 4: Eigene Funktion

def enthaelt(liste, artikel):
    enthalten = False
    for item in liste:
        if item == artikel:
            enthalten = True
    return enthalten


# Schritt 5: Testfälle

assert (enthaelt(einkaufsliste, "Butter")) == False     # Artikel fehlt
assert (enthaelt(einkaufsliste, "Marmelade")) == True   # Artikel vorhanden
assert (enthaelt([], "Marmelade")) == False             # leere Liste

# Zusatzaufgabe: Artikel nur hinzufügen, wenn er noch nicht auf der Liste steht

def hinzufuegen(liste, artikel):
    