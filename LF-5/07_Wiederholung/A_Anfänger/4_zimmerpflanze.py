
feuchte = int(input("Gemessene Bodenfeuchte in Prozent: "))

if feuchte < 30:
    print("Bitte gießen!")
elif feuchte > 80:
    print("Zu nass - eine Woche nicht gießen.")
else:
    print("Alles gut.")

