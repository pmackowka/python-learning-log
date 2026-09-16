"""Sprawdzanie czy słowo jest palindromem - trzy warianty tej samej funkcji
(pełne if/else, ternary, dwuwskaźnikowo w pętli while), każdy wywołany osobno.

Pytanie 12 - napisz funkcję sprawdzającą czy podane słowo jest palindromem.
Uruchom funkcję aby sprawdzić czy palindromami są słowa "kajak" i "anakonda".

Anna # gawron # radar
"""


def sprawdz_czy_palindrom_v1(slowo):
    slowo_odwrocone = slowo[
        ::-1
    ]  # utworz zmienna slowo_odwrocone odwracając przy użyciu sliców
    if slowo == slowo_odwrocone:  # jeśli slowo jest równe slowo_odwrocone
        return True  # zwróć True
    else:  # w przeciwnym wypadku
        return False  # zwróć False


def sprawdz_czy_palindrom_v2(slowo):
    return True if slowo == slowo[::-1] else False
    # zwróć True jeśli slowo jest równe samemu sobie przeczytanemu od tyłu, w przeciwnym wypadku zwróć False


def sprawdz_czy_palindrom_v3(slowo):
    poczatek = 0  # stwórz indeks poczatkowy równy 0
    koniec = (
        len(slowo) - 1
    )  # stwórz indeks końcowy równy długości stringa zmniejszonej o 1
    while (
        poczatek <= koniec
    ):  # wykonuj pętlę dopóki indeks poczatkowy jest mniejszy lub równy indeksowi końcowemu
        if (
            slowo[poczatek] != slowo[koniec]
        ):  # jeśli wartosc zmiennej slowo od indeksu początkowego jest różna od wartości od indeksu końcowego
            return False  # zwróć False
        else:  # w przeciwnym wypadku
            poczatek += 1  # zwiększ indeks początkowy o 1
            koniec -= 1  # zmniejsz indeks końcowy o 1
    return True  # jeśli funkcja dotarła do tego miejsca, to znaczy że słowo jest palindromem i funkcja zwraca True


for wariant in (
    sprawdz_czy_palindrom_v1,
    sprawdz_czy_palindrom_v2,
    sprawdz_czy_palindrom_v3,
):
    print(wariant("kajak"))
    print(wariant("anakonda"))


def palindrome(slowo):
    poczatek = 0
    koniec = len(slowo) - 1

    while poczatek <= koniec:
        if slowo[poczatek] != slowo[koniec]:
            return print(f"{slowo} nie jest palindromem")
        else:
            poczatek += 1
            koniec -= 1
    return print(f"{slowo} jest palindromem")


palindrome("kajakk")
