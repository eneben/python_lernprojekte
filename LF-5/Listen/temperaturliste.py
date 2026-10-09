temps = [-2, -4, 1, 3, 0, -1]

def froststunden(temps):
    anzahl = 0
    for temp in temps:
        if temp < 0:
            anzahl += 1
    return anzahl

assert froststunden([0, -1, 1]) == 1

print(froststunden(temps))