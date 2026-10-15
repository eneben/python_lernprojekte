
def in_minuten(uhrzeit):
    stunden_minuten_liste = uhrzeit.split(":")
    stunden = int(stunden_minuten_liste[0])
    minuten = int(stunden_minuten_liste[1])
    minuten_seit_mitternacht = stunden * 60 + minuten
    return minuten_seit_mitternacht

def zu_uhrzeit(minuten):
    stunden = minuten // 60
    uebrige_minuten = minuten % 60
    return f"{stunden:02d}:{uebrige_minuten:02d}"

def dauer(start, ende):
    dauer_minuten = in_minuten(ende) - in_minuten(start)
    return dauer_minuten

assert in_minuten("08:45") == 525
assert zu_uhrzeit(5) == "00:05"
assert dauer("07:50", "16:20") == 510

print("Alle Tests durchgelaufen.")

eingabe_beginn = input("Stempeluhr-Eintrag Arbeitsbeginn (digitale Zeitanzeige, z.B. 07:45): ")
eingabe_ende = input("Stempeluhr-Eintrag Arbeitsende (digitale Zeitanzeige, z.B. 17:10): ")

print(f"Arbeitszeit: {zu_uhrzeit(dauer(eingabe_beginn, eingabe_ende))} Stunden")