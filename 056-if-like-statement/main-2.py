"""LAB - Operacje na plikach w wyrażeniach logicznych
Utwórz plik i wpisz do niego kilka słów, np co widzisz za oknem :)

Utwórz funkcję, która jako parametr przyjmuje ścieżkę dostępu do pliku i zwraca ilość słów w tym pliku, jeśli potrzebujesz kroków pomocniczych oto i one:
Otwórz plik poleceniem open (możesz skorzystać z parametru encoding="utf-16" jeżeli trzeba)
Wczytaj plik do zmiennej korzystając z funkcji read()
"Rozbij" wczytaną zawartość korzystając z funkcji split()
Policz ile elementów jest zwracanych przez funkcję split()
Zwróć tą wartość
W głównym skrypcie:
zadeklaruj zmienną path i przypisz jej wartość wskazującą na plik utworzony na początku
napisz polecenie warunkowe, które sprawdzi czy plik istnieje
jeśli tak, wywoła funkcję, policzy ilość słów w pliku i wyświetli o tym informację
napisz wyrażenie logiczne, które wykona te same czynności, co wcześniej napisana instrukcja if"""

import os  # Import biblioteki do obsługi systemu plików
from pathlib import Path


# Funkcja do liczenia ilości słów w pliku
def count_words_in_file(file_path):
    """
    Liczy ilość słów w pliku wskazanym przez file_path.
    """
    try:
        # Otwieranie pliku w trybie odczytu
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()  # Wczytanie całej zawartości pliku
            words = content.split()  # Rozbicie zawartości na listę słów
            return len(words)  # Zwrócenie liczby słów
    except FileNotFoundError:
        print(f"Plik {file_path} nie istnieje.")
        return 0  # Zwracamy 0 w przypadku błędu


# Ścieżka do pliku
path = Path(__file__).parent / "main-2-file-1.txt"

# Sprawdzenie, czy plik istnieje, za pomocą instrukcji if
if os.path.isfile(path):  # Sprawdzanie, czy plik istnieje
    word_count = count_words_in_file(path)  # Wywołanie funkcji liczącej słowa
    print(f"Ilość słów w pliku '{path}': {word_count}")
else:
    print(f"Plik {path} nie istnieje.")

# Wyrażenie logiczne, które wykona te same czynności
os.path.isfile(path) and print(
    f"Ilość słów w pliku '{path}': {count_words_in_file(path)}"
) or print(f"Plik {path} nie istnieje.")
