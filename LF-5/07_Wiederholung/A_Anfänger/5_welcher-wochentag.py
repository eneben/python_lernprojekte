zahl = int(input("Gib eine Zahl zwischen 1 und 7 ein: "))
match zahl:
    case 1:
        print("Montag")
    case 2:
        print("Dienstag")
    case 3:
        print("Mittwoch")
    case 4:
        print("Donnerstag")
    case 5:
        print("Freitag")
    case 6 | 7:
        print("Wochenende")
    case _:
        print("Ungültige Eingabe")