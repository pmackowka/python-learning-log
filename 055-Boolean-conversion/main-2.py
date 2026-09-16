"""LAB - Automatyczna konwersja do typu logicznegoLAB
Poniżej masz jedno zadanie - opisane mniej lub bardziej dokładnie - sam wybierz jaki opis preferujesz. Rozwiązując zadanie staraj się, gdzie się da, korzystać z automatycznej konwersji do typu logicznego (niezależnie od tego, czy to dobra praktyka czy nie)


Zadanie w wersji skróconej:
Napisz skrypt, który będzie wyświetlał użytkownikowi zestaw opcji do wyboru:
['load data', 'export data', 'analyze & predict']
Skrypt ma:
działać tak długo, aż użytkownik niczego nie wybierze i naciśnie enter
po wprowadzeniu wartości ma sprawdzać czy ta wartość jest liczbą
jeśli nie jest liczbą ma wyświetlić o tym komunikat
jeśli jest liczbą, to ma sprawdzić czy jest jednym z dopuszczalnych numerów opcji
jeśli tak, to ma wyświetlić komunikat z numerem wybranej opcji i treścią
jeśli nie, to ma wyświetlić komunikat o tym, że wybrana jest niepoprawna opcja
"""

# Lista opcji do wyboru
options = ["load data", "export data", "analyze & predict"]

while True:
    # Wyświetlanie menu
    print("\nWybierz opcję:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("Naciśnij Enter, aby zakończyć.")

    # Pobranie wyboru od użytkownika
    user_input = input("Twój wybór: ")

    # Wyjście z pętli, jeśli użytkownik naciśnie Enter
    if user_input == "":
        print("Koniec programu. Do zobaczenia!")
        break

    # Sprawdzanie, czy wprowadzono liczbę
    if not user_input.isdigit():
        print("Niepoprawny wybór! Wprowadź numer opcji.")
        continue

    # Konwersja na liczbę
    option_number = int(user_input)

    # Sprawdzanie, czy numer opcji jest poprawny
    if 1 <= option_number <= len(options):
        print(f"Wybrano opcję {option_number}: {options[option_number - 1]}")
    else:
        print("Niepoprawny numer opcji! Wybierz poprawny numer.")
