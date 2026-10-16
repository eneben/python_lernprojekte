ablesungen = [12450, 12731, 12988, 13302, 13560, 13801]
monate = ["Jan", "Feb", "Mär", "Apr", "Mai"]

def verbrauch_je_monat(staende):
    verbrauch_je_monat = []
    for i in range(1, len(staende)):
        verbrauch_je_monat.append(staende[i] - staende[i-1])
    return verbrauch_je_monat

verbrauch_je_monat(ablesungen)

def index_maximum(werte):
    max_index = 0
    verbrauch = verbrauch_je_monat(werte)
    for i in range(1, len(verbrauch)):
        if verbrauch[i] > verbrauch[max_index]:
            max_index = i
    return max_index

def durchschnitt(staende):
    verbrauch = verbrauch_je_monat(staende)
    summe = 0
    for monats_verbrauch in verbrauch:
        summe = summe + monats_verbrauch
    durchschnitt = summe / len(verbrauch)
    return durchschnitt

def ueber_durchschnitt(staende, monate):
    verbrauch = verbrauch_je_monat(staende)
    durchschnittswert = durchschnitt(staende)
    ueber_durchschnitt_indizes = []
    ueber_durchschnitt_monate = []
    for i in range(0, len(verbrauch)):
        if verbrauch[i] > durchschnittswert:
            ueber_durchschnitt_indizes.append(i)
    for i in range(0, len(monate)):
        if i in ueber_durchschnitt_indizes:
            ueber_durchschnitt_monate.append(monate[i])
    return ueber_durchschnitt_monate


def ausgabe(staende, monate):
    print("Verbrauch: ", verbrauch_je_monat(staende))
    print("Höchster Verbrauch im ", monate[index_maximum(staende)])
    print("Durchschnitt: ", durchschnitt(staende), " kWh")
    print("Über dem Durchschnitt: ", " und ".join(ueber_durchschnitt(staende, monate)))

ausgabe(ablesungen, monate)