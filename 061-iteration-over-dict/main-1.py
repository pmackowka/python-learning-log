# Budowanie słownika przez zip() dwóch list, iteracja po kluczach i po wartościach.
workDays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months_roman = [
    "I",  # Styczeń
    "II",  # Luty
    "III",  # Marzec
    "IV",  # Kwiecień
    "V",  # Maj
    "VI",  # Czerwiec
    "VII",  # Lipiec
    "VIII",  # Sierpień
    "IX",  # Wrzesień
    "X",  # Październik
    "XI",  # Listopad
    "XII",  # Grudzień
]

monthDays = dict(zip(workDays, months_roman))
print(monthDays)

print("-" * 20)

for key in monthDays:
    print(key, monthDays[key])

print("-" * 20)

for value in monthDays.values():
    print(value)
