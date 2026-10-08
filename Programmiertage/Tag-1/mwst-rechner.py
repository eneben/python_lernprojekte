#Eingabe
nettowert = float(input("Nettopreis eingeben: "))
steuersatz = int(input("Mehrwertsteuersatz 19 oder 7? "))

#Verarbeitung
def rechnung(a, b):
    return a + (a * b / 100)

ergebnis = None

if steuersatz == 7 or steuersatz == 19:
    ergebnis = rechnung(nettowert, steuersatz)

else:
    print("Ungültiger Steuersatz")

#Ausgabe
if ergebnis is not None:
    print(f"Der Bruttopreis beträgt {ergebnis:.2f} EUR")