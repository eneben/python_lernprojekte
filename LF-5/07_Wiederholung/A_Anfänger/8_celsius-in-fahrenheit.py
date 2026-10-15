def celsius_zu_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(celsius_zu_fahrenheit(20))

assert celsius_zu_fahrenheit(0) == 32
assert celsius_zu_fahrenheit(100) == 212
assert celsius_zu_fahrenheit(-40) == -40

print("Alle Tests bestanden.")