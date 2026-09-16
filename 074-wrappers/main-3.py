"""LAB - Wrapper dla funkcji, dekorowanie funkcji
Pracujesz w  SZIN (Super Zwariowany Instytut Naukowy).  W SZIN dużą wagę przykłada się do tego, aby funkcje działały szybko! Dlatego powstał pomysł, aby każda strategiczna funkcja posiadała wrapper, który zmierzy czas wykonania danej funkcji.

Oto funkcja, dla której trzeba stworzyć wrapper:

def get_sequence(n):

    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

# Możesz uruchomić funkcję z różnym argumentem n, np tak:

print(get_sequence(5))

Na moim komputerze wykonanie funkcji z n=18 trwało 3 sekundy, n=19 - 6 sekund, a n=20 - 14 sekund. Sam dobierz wartość argumentu, który spowoduje wykonanie funkcji w rozsądnym czasie, a jednocześnie będzie trwało dłużej niż sekundę.
Jeżeli już wiesz jak to zrobić - do dzieła! Jeśli potrzebujesz wskazówek - patrz niżej:
Zaimportuj moduł time
Zdefiniuj funkcję wrapper_time przyjmującą jako argument inną funkcję: a_function
W tej funkcji zdefiniuj nową funkcję a_wrapped_function, która:
jako argument przyjmuje wszystkie możliwe argumenty
w zmiennej time_start zapamięta aktualny czas
w zmiennej v zostanie zapamiętany wynik wywołania funkcji a_function (wywołując ją należy przekazać wszystkie potrzebne parametry)
w zmiennej time_stop zapamiętaj aktualny czas
Wyświetl komunikat o treści "Funkcja <tutaj_nazwa_funkcji> wykonana w czasie <tutaj wynik odejmowania time_stop - time_start>"
zwróć zmienną v
Zwróć funkcję a_wrapped_function
Funkcja tworząca wrapper jest gotowa - teraz trzeba jej użyć:
Do wrapper_get_sequence przypisz wynik funkcji wrapper_time wywołanej z argumentem wskazującym na oryginalną funkcję get_sequence
Uruchom tą funkcję wyświetlając jej wynik, np. tak:
print(wrapper_get_sequence(18))"""

import time


def wrapper_time(fun):

    def a_wrapped_function(*args, **kwargs):

        time_start = time.time()
        v = fun(*args, **kwargs)
        time_stop = time.time()
        print(f">>>>>Function {fun.__name__} executed in {time_stop - time_start}")

        return v

    return a_wrapped_function


def get_sequence(n):

    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


# print(get_sequence(10))

wrapper_get_sequence = wrapper_time(get_sequence)

print(wrapper_get_sequence(10))

# >>>>>Function get_sequence executed in 0.0006129741668701172
# 553.037109375
