wochenbetrag = int(input("Wie viel legst du pro Woche zurück? "))

dauer = 120 // wochenbetrag

if (120 % wochenbetrag > 0):
    dauer += 1

print(f"Du brauchst {dauer} Wochen.")
