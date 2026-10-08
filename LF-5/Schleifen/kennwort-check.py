# Ein Info-Terminal im Foyer soll nach einem
# Kennwort fragen – höchstens dreimal. Bei
# richtigem Kennwort erscheint „Willkommen“,
# sonst nach drei Fehlversuchen „Gesperrt“.

eingaben = 0
kennwort_richtig = False

while eingaben < 3 and not kennwort_richtig:
    kennwort = input("Kennwort: ")
    if kennwort == "Kiosk24":
        kennwort_richtig = True
    else:
        eingaben += 1

if kennwort_richtig:
    print("Willkommen")
else:
    print("Gesperrt")