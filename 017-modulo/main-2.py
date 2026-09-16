# Sprawdź czy liczba a jest podzielna przez b. Jeśli tak - wypisz True, jeśli nie - False.

a = 123454321
b = 11111


def czy_podzielna(liczba_a, liczba_b):
    return (liczba_a % liczba_b) == 0


print(czy_podzielna(a, b))

print(True if a % b == 0 else False)
