# Dla podanego słownika S napisz kod sprawdzający czy liczba 7430 znajduje się wśród kluczy słownika.

# Jeśli tak - wypisz True.

# Jeśli nie - False.

S = {x: x + 1 for x in range(10000) if x % 23 == 0}

if 7430 in S:
    print(True)
else:
    print(False)

print("###")

print(True if 7430 in S else False)
