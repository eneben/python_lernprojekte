# Ein Webserver schreibt zu jeder Anfrage einen Statuscode ins Log.
# Die Admin will wissen, wie oft ein bestimmter Code auftaucht.

codes = [200, 404, 200, 500, 404, 200]

def wie_oft(codes, code):
    anzahl = 0
    for single_code in codes:
        if single_code == code:
            anzahl += 1
    return anzahl

assert wie_oft(codes, 404) == 2
assert wie_oft(codes, 301) == 0
assert wie_oft([], 404) == 0
print("All tests passed.")