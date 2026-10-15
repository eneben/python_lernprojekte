def dreieck_art(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c or b + c > a or a + c > b:
            if a == b == c:
                return "Dies ist ein gleichseitiges Dreieck."
            elif a == b or a == c or b == c:
                return "Dies ist ein gleichschenkliges Dreieck."
            else:
                return "Dies ist ein unregelmäßiges Dreieck."
        else:
            return("Kein Dreieck: Zwei Seiten müssen zusammen größer sein als die dritte.")
    else:
        return("Kein Dreieck: Keine Seite darf als Länge 0 oder einen negativen Wert haben.")

def ausgabe_dreieck_art(a, b, c):
    print(f"Seiten: {a, b, c} - Ergebnis: {dreieck_art(a, b, c)}")

ausgabe_dreieck_art(3, 3, 3)
ausgabe_dreieck_art(5, 5, 8)
ausgabe_dreieck_art(8, 5, 5)
ausgabe_dreieck_art(3, 4, 5)
ausgabe_dreieck_art(1, 2, 3)
ausgabe_dreieck_art(0, 4, 4)