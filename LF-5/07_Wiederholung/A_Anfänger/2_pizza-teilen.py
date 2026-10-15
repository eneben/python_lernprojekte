pizzen = 3
stuecke_pro_pizza = 8
personen = 5

gesamt = pizzen * stuecke_pro_pizza
stuecke_pro_person = gesamt // personen
uebrige_stuecke = gesamt % personen

print(f"Stücke insgesamt: {gesamt} - Jede Person bekommt {stuecke_pro_person}. - Übrig bleiben: {uebrige_stuecke}")
