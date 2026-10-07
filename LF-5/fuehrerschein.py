def fahrbereit(alter, hat_fuehrerschein):
    if alter >= 18 and hat_fuehrerschein == True:
        print("Du darfst fahren!")
    else:
        print("Du darfst nicht fahren!")

alter = int(input("Bitte gib dein Alter ein: "))
hatF = input("Haben Sie einen Führerschein? (ja/nein)")

hat_fuehrerschein_boolean = hatF in ["ja", "yes", "True", "true"]

fahrbereit(alter, hat_fuehrerschein_boolean)