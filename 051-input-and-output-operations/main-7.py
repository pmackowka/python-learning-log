# Jak main-6.py, ale bez zapisu do plików - tylko klasyfikacja i wypisanie na ekran.
import os

# Pobranie nazwy pliku od użytkownika
filename = input("Enter filename with web addresses to read: ")

# Sprawdzanie, czy plik istnieje
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename = input("Enter filename to read: ")

# Inicjalizacja pustej listy do przechowywania adresów stron
webaddresses = []

# Otwieranie pliku w trybie odczytu
with open(filename, "r") as file:
    for line in file:
        # Usuwanie znaków nowej linii (\n) z każdej linii
        webaddresses.append(line.replace("\n", ""))

# Sprawdzanie i klasyfikowanie stron na polskie i inne
for line in webaddresses:
    if line.endswith(".pl"):  # Jeśli adres kończy się na '.pl'
        print(line, "is a polish web page")
    else:
        print(line, "is not a polish web page")
