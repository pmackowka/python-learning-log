# input() nazwy katalogu i pliku - wyświetlanie właściwości pliku
# (data modyfikacji, rozmiar, ścieżka względna).
import os
import time

# Pobranie nazwy katalogu od użytkownika.
dir = input("enter directory name: ")

# Sprawdzenie, czy wprowadzona nazwa odnosi się do istniejącego katalogu.
if not os.path.isdir(dir):
    print(
        "%s must be a directory" % dir
    )  # Jeśli katalog nie istnieje, wyświetla komunikat.
else:
    # Pobranie nazwy pliku w zadanym katalogu.
    file = input("enter filename saved in directory %s: " % dir)

    # Utworzenie pełnej ścieżki do pliku przy użyciu os.path.join.
    path = os.path.join(dir, file)

    # Sprawdzenie, czy plik istnieje.
    if not os.path.isfile(path):
        print(
            "File %s does not exist!" % path
        )  # Jeśli plik nie istnieje, wyświetla komunikat.
    else:
        # Wyświetlanie właściwości pliku.
        print("displaying properties of file %s" % path)

        # Ostatnia modyfikacja pliku, wyrażona jako czas lokalny.
        print("Last modified date", time.localtime(os.path.getmtime(path)))

        # Rozmiar pliku w bajtach.
        print("Size in bytes", os.path.getsize(path))

        # Wyświetlenie bieżącego katalogu roboczego.
        print("Current directory is: ", os.getcwd())

        # Relatywna ścieżka do pliku względem bieżącego katalogu roboczego.
        print("Relative path to the file is", os.path.relpath(path))
