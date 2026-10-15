# Praxisaufgabe · Die Klasse Parkhaus
# Ein Parkhaus hat eine feste Zahl an Plätzen. Autos fahren ein und aus.
# Die Zahl der belegten Plätze darf nur über Methoden geändert werden.

class Parkhaus:
    def __init__(self, name, plaetze):
        self.name = name
        self.__plaetze = plaetze
        self.__belegt = 0

    def einfahren(self):
        if self.__belegt < self.__plaetze:
            self.__belegt += 1
            return True
        return False

    def ausfahren(self):
        if self.__belegt >= 1:
            self.__belegt -= 1
            return True
        return False

    def freie_plaetze(self):
        return self.__plaetze - self.__belegt

    def __str__(self):
        return (f"Parkhaus {self.name}: {self.freie_plaetze()} von {self.__plaetze} frei")

am_markt = Parkhaus("Am Markt", 2)

assert am_markt.name == "Am Markt"
assert am_markt.freie_plaetze() == 2

assert am_markt.einfahren() is True
assert am_markt.freie_plaetze() == 1

assert am_markt.einfahren() is True
assert am_markt.freie_plaetze() == 0

assert am_markt.einfahren() is False
assert am_markt.freie_plaetze() == 0

assert am_markt.ausfahren() is True
assert am_markt.freie_plaetze() == 1

print(f"{am_markt.name} - freie Plätze: {am_markt.freie_plaetze()}")
print("Alle Tests bestanden")

print("Freie Plätze vorher:", am_markt.freie_plaetze())
am_markt._belegt = 99
print("Freie Plätze nachher:", am_markt.freie_plaetze())

print("Prüfung von __str__:")
print(am_markt)

