# Własny iterator (__iter__/__next__) generujący kolejne daty, z pomiarem czasu wykonania.
import datetime as dt  # Import modułu datetime i nadaje mu alias "dt" dla łatwiejszego użycia.
import sys  # Import modułu sys, który pozwala na uzyskanie informacji o systemie i użycie metod takich jak getsizeof().

start = (
    dt.datetime.now()
)  # Pobiera aktualny czas i datę jako obiekt datetime i zapisuje w zmiennej 'start'.
print(
    f"Execution started at: {start}"
)  # Wyświetla informację o rozpoczęciu wykonania programu.


# Definicja klasy MillionDays jako iteratora do generowania kolejnych dat.
class MillionDays:
    def __init__(
        self, year, month, day, maxdays
    ):  # Konstruktor klasy przyjmuje rok, miesiąc, dzień początkowy oraz maksymalną liczbę dni do wygenerowania.
        self.date = dt.date(
            year, month, day
        )  # Tworzy obiekt daty na podstawie podanych wartości i przypisuje do atrybutu 'date'.
        self.maxdays = maxdays  # Przechowuje maksymalną liczbę dni do iteracji w atrybucie 'maxdays'.

    def __next__(
        self,
    ):  # Definicja metody __next__, która zwraca kolejną datę w iteracji.
        if (
            self.maxdays <= 0
        ):  # Sprawdza, czy liczba pozostałych dni wynosi 0 lub mniej.
            raise StopIteration()  # Jeśli tak, przerywa iterację, zgłaszając wyjątek StopIteration.
        ret = self.date  # Przypisuje bieżącą datę do zmiennej tymczasowej 'ret'.
        self.date += dt.timedelta(
            days=1
        )  # Zwiększa datę o 1 dzień za pomocą obiektu timedelta.
        self.maxdays -= 1  # Zmniejsza liczbę pozostałych dni do iteracji o 1.
        return ret  # Zwraca bieżącą datę.

    def __iter__(self):  # Definicja metody __iter__, która zwraca sam obiekt iteratora.
        return self


# Tworzenie instancji klasy MillionDays, która generuje 2 500 000 kolejnych dni począwszy od 1 stycznia 2000 r.
md = MillionDays(2000, 1, 1, 2_500_000)
print(
    f"size of MillionDays is {sys.getsizeof(md)}"
)  # Wyświetla rozmiar pamięci zajmowanej przez obiekt md.

# Iteracja przez wszystkie daty generowane przez obiekt md.
for d in md:
    pass  # Dla każdej daty nie wykonuje żadnej akcji (symboliczna pętla).

stop = dt.datetime.now()  # Pobiera aktualny czas i datę jako obiekt datetime po zakończeniu pętli i zapisuje w zmiennej 'stop'.
print(f"Execution stop at: {stop}")  # Wyświetla czas zakończenia wykonania programu.

# Wyświetla całkowity czas wykonania programu, obliczony jako różnica między 'stop' i 'start'.
print(f"Total time: {stop - start}")
