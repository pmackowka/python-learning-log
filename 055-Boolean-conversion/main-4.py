# Menu wyboru opcji w pętli while - ta sama logika najpierw bez komentarzy, potem z komentarzami.
def DisplayOptions(options):
    for i in range(len(options)):
        print(f"{i + 1} - {options[i]}")

    choice = input("Select option above or press enter to exit: ")
    return choice


choice = "x"
options = ["load data", "export data", "analyze & predict"]

while choice:
    choice = DisplayOptions(options)

    # executed only if something was entered
    if choice:
        try:
            choice_num = int(choice) - 1
            if choice_num >= 0 and choice_num < len(options):
                print(f"you have selected {choice_num + 1} - {options[choice_num]}")
            else:
                print("choose a value from a list or press enter")
        except:
            print("You need to enter a number")
    else:
        print("----- END -----")


print(20 * "-")


def DisplayOptions(options):
    # Funkcja, która wyświetla dostępne opcje z listy oraz zwraca wybór użytkownika
    for i in range(len(options)):
        # Iterujemy przez listę opcji i wyświetlamy każdą z nich z przypisanym numerem
        print(f"{i + 1} - {options[i]}")

    # Pobieramy wybór użytkownika; jeśli użytkownik nic nie wpisze, zwracany będzie pusty ciąg
    choice = input("Select option above or press enter to exit: ")
    return choice  # Zwracamy wybór użytkownika (może to być numer opcji lub pusty ciąg)


# Inicjalizacja zmiennej choice na wartość 'x', aby warunek pętli while był spełniony przy pierwszym przebiegu
choice = "x"
# Definicja listy opcji, które będą wyświetlane użytkownikowi
options = ["load data", "export data", "analyze & predict"]

# Pętla while działa, dopóki zmienna choice nie jest pusta (czyli użytkownik nie nacisnął Enter bez wpisywania wartości)
while choice:
    # Wywołanie funkcji DisplayOptions, która wyświetla opcje i zwraca wybór użytkownika
    choice = DisplayOptions(options)

    # Warunek sprawdza, czy użytkownik coś wpisał
    if choice:
        try:
            # Próba zamiany wpisanego przez użytkownika tekstu na liczbę całkowitą (numer opcji)
            choice_num = (
                int(choice) - 1
            )  # Odejmujemy 1, aby dopasować numer opcji do indeksu listy
            if choice_num >= 0 and choice_num < len(options):
                # Jeśli numer opcji jest poprawny (mieści się w zakresie indeksów listy)
                print(f"you have selected {choice_num + 1} - {options[choice_num]}")
            else:
                # Jeśli numer opcji jest spoza zakresu, informujemy użytkownika o poprawnych wartościach
                print("choose a value from a list or press enter")
        except:
            # Obsługa wyjątku, jeśli użytkownik nie wpisał liczby (np. wpisał tekst zamiast numeru)
            print("You need to enter a number")
    else:
        # Blok else działa, gdy zmienna choice jest pusta (użytkownik nacisnął Enter bez wpisywania wartości)
        print("----- END -----")  # Wyświetlamy komunikat końcowy
