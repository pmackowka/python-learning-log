# Sprawdź i wypisz (True lub False) czy największy element na liście A jest większy niż liczba 99.


A = [x**2 + 3 for x in range(10)]


print(max(A) > 99)

if max(A) > 99:
    print(True)
else:
    print(False)
