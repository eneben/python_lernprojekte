# Aufgabe: Programm, mit dem Artikel, Einzelpreis und Menge erfasst und daraus der Gesamtpreis und die Mehrwertsteuer berechnet werden können. 
# Am Ende soll ein Kassenbon ausgegeben werden.
# Erwartete Eingabe: Artikel, Einzelpreis, Menge.
# Ausgabe: Kassenbon, Artikel, Einzelpreis, Menge, Nettosumme, MwSt., Leerzeile, Gesamtpreis

import sys

# Eingabe:

artikel = (input("Artikel eingeben: "))
preis_einzel = float(input("Einzelpreis eingeben: ").replace(",", "."))
menge = int(input("Wie oft wird der Artikel gekauft? "))
steuersatz = int(input("Mehrwertsteuersatz 19 oder 7? "))

# Funktionen und Definitionen:

def rechnung_preis_menge(einzelpreis, anzahl):
    return einzelpreis * anzahl

def rechnung_mwst(preis, steuer):
    return preis * steuer / 100

def rechnung_preis_gesamt(preis, mwst):
    return preis + mwst

preis_ohne_mwst = None
preis_inkl_mwst = None
mwst = None

# Verarbeitung:

if menge > 0 and preis_einzel > 0:
    preis_ohne_mwst = rechnung_preis_menge(preis_einzel, menge)

elif menge <= 0:
    print("Die Menge muss über 0 betragen.")
    sys.exit()

elif preis_einzel <= 0:
    print("Der Preis muss über 0 betragen.")
    sys.exit()

else:
    print("Fehler_1")

if preis_ohne_mwst is not None:

    if steuersatz == 7 or steuersatz == 19:
        mwst = rechnung_mwst(preis_ohne_mwst, steuersatz)
        preis_inkl_mwst = rechnung_preis_gesamt(preis_ohne_mwst, mwst)

    else:
        print("Ungültiger Steuersatz")
        sys.exit()

else:
    print("Fehler_2")

#Ausgabe

if mwst is not None and preis_inkl_mwst is not None:
    print("\n--- Kassenbon ---")
    print(f"\n{'Artikel:':<20}{artikel:>10}")
    print(f"{'Einzelpreis:':<20}{preis_einzel:>10.2f} €")
    print(f"\n{'Menge:':<20}{menge:>10}")
    print(f"{'Nettopreis:':<20}{preis_ohne_mwst:>10.2f} €")
    print(f"{'MwSt. (' + str(steuersatz) + ' %):':<20}{mwst:>10.2f} €")
    print(f"\n{'Gesamtpreis:':<20}{preis_inkl_mwst:>10.2f} €")
    
else:
    print("Fehler_3")


# Testwerte // Ausgabe

# 1. Test
# Kaffee / 2,50 / 3 / 20 // Ungültiger Steuersatz

# 2. Test
# Äpfel / 0.5 / -2 / 7 // Die Menge muss über 0 betragen.

# 3. Test
# Kekse / 2 / 30 / 7 // 
# --- Kassenbon ---
# 
# Artikel:                 Kekse
# Einzelpreis:              2.00 €
# 
# Menge:                      30
# Nettopreis:              60.00 €
# MwSt. (7 %):              4.20 €
# 
# Gesamtpreis:             64.20 €