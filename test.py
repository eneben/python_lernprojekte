#Eingabe
artikel = "Kaffee"
menge = int(input("Menge: "))
preis = float(input("Preis: ").replace(",", "."))

#Verarbeitung
gesamtpreis = menge * preis

#Ausgabe
print("\n--- Kassenbon ---")
print("Artikel:", artikel)
print(f"Preis: {preis:.2f} €")
print("Menge:", menge)
print(f"Gesamtpreis: {gesamtpreis:.2f} €")