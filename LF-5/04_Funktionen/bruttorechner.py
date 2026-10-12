# Netto in Brutto umrechnen. Alle Artikel sollen 19 % Mehrwertsteuer berechnen, 
# nur Bücher 7 %. Die Preise sollen auf Cent gerundet sein.

def brutto_mit_satzeingabe(netto, satz = 0.19):
    return round(netto * satz + netto, 2) 

assert brutto_mit_satzeingabe(100) == 119.00
assert brutto_mit_satzeingabe(100, 0.07) == 107.00
assert brutto_mit_satzeingabe(20, 0.07) == 21.40

beispiel_preis = brutto_mit_satzeingabe(100, 0.07)
print(f"Beispielpreis mit zwei Nachkommastellen: {beispiel_preis:.2f} €")

def brutto_mit_abfrage(netto):
    satz = 0.19
    buch_abfrage = input("Handelt es sich um ein Buch? ja / nein ").strip().lower()
    if buch_abfrage == "ja":
        satz = 0.07
    return round(netto * satz + netto,2)

print("2 Wert 100: ", brutto_mit_abfrage(100))
print("2 Wert 10: ", brutto_mit_abfrage(10))