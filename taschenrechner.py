#Eingabe
zahl1 = float(input("Erste Zahl eingeben: "))
operator = input("Operator (+, -, x, /): ")
zahl2 = float(input("Zweite Zahl eingeben: "))


#Verarbeitung
def addition(a, b):
    return a + b

def subtraktion(a, b):
    return a - b

def multiplikation(a, b):
    return a * b

def division(a, b):
    return a / b

ergebnis = None

if operator == "+":
    ergebnis = addition(zahl1, zahl2)

elif operator == "-":
    ergebnis = subtraktion(zahl1, zahl2)

elif operator == "x":
    ergebnis = multiplikation(zahl1, zahl2)

elif operator == "/":
    if zahl2 == 0: 
        print("Durch Null kann man nicht teilen.")
    else:
        ergebnis = division(zahl1, zahl2)

else:
    print("Ungültiger Operator")

#Ausgabe
if ergebnis is not None:
    print("Ergebnis: ", round(ergebnis, 10))