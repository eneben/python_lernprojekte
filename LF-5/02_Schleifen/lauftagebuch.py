# Praxisaufgabe Kapitel 07 · Das Lauftagebuch
# Eine Läuferin notiert die Kilometer ihrer Läufe in einer Liste.

bsp_laeufe = [5.2, 3.8, 10.0, 7.5, 4.9]

# for testing:
# bsp_laeufe = []

# Schritt 1: Gesamtstrecke
def gesamt_km(laeufe):
    strecke = 0
    for lauf in laeufe:
        strecke = strecke + lauf
    return strecke


# Schritt 2: Längster Lauf
def laengster_lauf(laeufe):
    if not laeufe:
        return 0
    lang = laeufe[0]
    for lauf in laeufe:
        if lauf > lang:
            lang = lauf
    return lang


# Schritt 3: Lange Läufe zählen
def anzahl_ab(laeufe, grenze):
    zaehler = 0
    for lauf in laeufe:
        if lauf >= grenze:
            zaehler += 1
    return zaehler


# Schritt 4: Ausgabe aller Ergebnisse, Gesamtstrecke gerundet
bsp_strecke = round(gesamt_km(bsp_laeufe), 1)
bsp_lang = laengster_lauf(bsp_laeufe)
grenze = 5
bsp_zaehler = anzahl_ab(bsp_laeufe, grenze)
print(f"Gesamt: {bsp_strecke} km. Längster Lauf: {bsp_lang} km. Läufe ab {grenze} km: {bsp_zaehler}.")


# Schritt 5: Testfälle
assert gesamt_km([3.5,5,8]) == 16.5
assert gesamt_km([]) == 0
assert laengster_lauf([3.5,5,8]) == 8
assert laengster_lauf([3.0]) == 3.0
assert laengster_lauf([]) == 0
assert anzahl_ab([3.5,5,8],5) == 2

# Zusatz: Durchschnitt berechnen und gegen leere Liste absichern
def durchschnitt(laeufe):
    if not laeufe:
        return 0
    durchschnitt = round(gesamt_km(laeufe) / len(laeufe),1)
    return durchschnitt

assert durchschnitt([]) == 0
assert durchschnitt([3.5,5,8]) == 5.5

print(f"Durchschnittliche Lauflänge: {durchschnitt(bsp_laeufe)} km.")


