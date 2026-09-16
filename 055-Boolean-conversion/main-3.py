"""LAB - Automatyczna konwersja do typu logicznegoLAB
Poniżej masz jedno zadanie - opisane mniej lub bardziej dokładnie - sam wybierz jaki opis preferujesz. Rozwiązując zadanie staraj się, gdzie się da, korzystać z automatycznej konwersji do typu logicznego (niezależnie od tego, czy to dobra praktyka czy nie)


Zadanie w wersji nieco bardziej rozbudowanej:
Do zmiennej options wpisz listę dostępnych opcji ['load data', 'export data', 'analyze & predict']
Do zmiennej choice przypisz wartość 'x'
Napisz funkcję DisplayOptions, przyjmującą jako argument listę opcji która wyświetla komunikat w rodzaju:
1 - load data
2 - export data
3 - analyze & predict
Select option above or press enter to exit:
oraz pobiera wprowadzoną przez użytkownika wartość. Funkcja ma wczytać wartość i zwrócić ją jako string (bez jakiejkolwiek kontroli)
Napisz pętlę while, która działa tak długo, jak zmienna choice ma jakąś wartość
W tej pętli do zmiennej choice wczytuj wynik zwracany przez funkcję DisplayOptions
Napisz polecenie if/else, które sprawdza czy choice nie jest pustym napisem
jeśli tak:
w bloku try/except skonwertuj choice do liczby choice_num typu int
jeśli się udało
jeśli wartość jest dopuszczalna (większa od 0 i mniejsza równa od ilości opcji - wyświetl informacje o tym co zostało wybrane
jeśli wartość nie jest dopuszczalna, wyświetl komunikat o tym, że dokonano nieprawidłowego wyboru
jeśli się nie udało - wyświetl informację wskazującą na to że ma być wprowadzana liczba
Jeśli nie:
wyświetl informację o zakończeniu działania programu"""

# Lista dostępnych opcji
options = ["load data", "export data", "analyze & predict"]

# Zmienna przechowująca wybór użytkownika
choice = "x"


# Funkcja wyświetlająca opcje i pobierająca wybór użytkownika
def DisplayOptions(options_list):
    """
    Wyświetla listę opcji oraz pobiera wybór użytkownika.

    :param options_list: lista dostępnych opcji
    :return: wartość wprowadzona przez użytkownika jako string
    """
    print("Dostępne opcje:")
    for idx, option in enumerate(options_list, start=1):
        print(f"{idx} - {option}")
    print("Select option above or press enter to exit:")
    return input("> ")


# Pętla wykonująca się dopóki choice nie jest pustym napisem
while choice:
    # Pobierz wybór użytkownika
    choice = DisplayOptions(options)

    # Sprawdzenie, czy wybór nie jest pusty
    if choice:
        try:
            # Konwersja wyboru na liczbę całkowitą
            choice_num = int(choice)

            # Sprawdzenie, czy wybór jest poprawny
            if 1 <= choice_num <= len(options):
                print(f"Wybrano opcję: {choice_num} - {options[choice_num - 1]}")
            else:
                print("Dokonano nieprawidłowego wyboru. Spróbuj ponownie.")
        except ValueError:
            # Obsługa błędu, gdy wybór nie jest liczbą
            print("Proszę wprowadzić poprawny numer opcji (liczbę).")
    else:
        # Komunikat kończący działanie programu
        print("Program zakończył działanie.")
