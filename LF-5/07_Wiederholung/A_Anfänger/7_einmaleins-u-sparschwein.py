# Einmaleins der 7 in der Ausgabe:

for x in range(1,11):
    print(x, "x 7 =", 7*x)

# Sparschwein: jede Woche 5 EUR. Wie viele Wochen, bis 50 EUR?

sparschwein = 0
wochen = 0

while sparschwein < 50:
    sparschwein += 5
    wochen += 1
print(f"Das Sparschwein enthält {sparschwein} EUR nach {wochen} Wochen.")