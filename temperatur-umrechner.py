# Aufgabe: Temperaturen am Morgen und am Mittag vergleichen und zusaetzlich von Celsius in Fahrenheit umrechnen

def difference(a, b):
    return round(a - b,2)

def conversion_to_fahrenheit(cel):
    return cel * 9/5 + 32

temp_morning = float(input("Temperatur morgens in °C: ").replace(",", "."))
temp_noon = float(input("Temperatur mittags in °C: ").replace(",", "."))

print("In Celsius betrug die Temperatur morgens ", temp_morning, " Grad und mittags ", temp_noon, " Grad.")

fahrenheit_morning = conversion_to_fahrenheit(temp_morning)
fahrenheit_noon = conversion_to_fahrenheit(temp_noon)

print("Das entspricht einer Temperatur von ", fahrenheit_morning, " Grad Fahrenheit morgens und von ", fahrenheit_noon, " Grad Fahrenheit mittags.")

if temp_morning > temp_noon:
    print("Die Temperatur morgens war höher als mittags. Der Unterschied beträgt in Celsius ", difference(temp_morning, temp_noon), 
          " Grad und in Fahrenheit ", difference(fahrenheit_morning, fahrenheit_noon), " Grad.")

elif temp_noon > temp_morning:
    print("Die Temperatur mittags war höher als morgens. Der Unterschied beträgt in Celsius ", difference(temp_noon, temp_morning), 
          " Grad und in Fahrenheit ", difference(fahrenheit_noon, fahrenheit_morning), " Grad.")

elif temp_morning == temp_noon:
    print("Die Temperatur morgens und mittags war gleich.")

else:
    print("Fehler")

