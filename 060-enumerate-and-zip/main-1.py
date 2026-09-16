# print(list(range(1, 13)))

workDays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

enumerateDays = list(enumerate(workDays))
print(enumerateDays)

print("-" * 20)

for key, value in enumerateDays:
    print("key", key, "value", value)

print("-" * 20)
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

merge = list(zip(months_roman, workDays))
print(merge)
# [('I', 1), ('II', 2), ('III', 3), ('IV', 4), ('V', 5), ('VI', 6), ('VII', 7), ('VIII', 8), ('IX', 9), ('X', 10), ('XI', 11), ('XII', 12)]

print("-" * 20)
for m, d in merge:
    print("Month:", m, "Day:", d)

print("-" * 20)
for key, (m, d) in enumerate(zip(months_roman, workDays)):
    print(key, m, d)
