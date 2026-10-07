def versand(kg):
    if kg <= 0:
        raise ValueError("Fehler. Das Gewicht muss über 0 betragen.")
    elif kg <= 1:
        return 3.90
    elif kg <= 5:
        return 5.90
    else:
        return 9.90

# assert versand(0) == "Fehler. Das Gewicht muss über 0 betragen."
assert versand(1) == 3.90
assert versand(5) == 5.90
assert versand(6) == 9.90

print("All tests passed.")
print(versand(0.9))
# print(versand(0))