# Der Drucker im Sekretariat protokolliert die
# Seitenzahl jedes Auftrags eines Tages.
# Die Verwaltung möchte wissen, wie viele Seiten
# insgesamt gedruckt wurden und wie viele
# Aufträge mehr als 10 Seiten hatten.

beispiel_auftraege = [12, 3, 40, 1, 8, 25]

def seiten_gesamt(auftraege):
    summe = 0
    for seiten in auftraege:
        summe = summe + seiten
    return summe

print(seiten_gesamt(beispiel_auftraege))

def grosse_auftraege(auftraege):
    summe = 0
    for seiten in auftraege:
        if seiten > 10:
            summe = summe + 1
    return summe

print(grosse_auftraege(beispiel_auftraege))