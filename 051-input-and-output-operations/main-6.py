# Wczytanie adresów www z pliku i rozdzielenie ich do dwóch plików wynikowych (.pl / inne).
import os

# Pobranie nazwy pliku z adresami stron od użytkownika
filename = input("Enter filename with web addresses to read: ")

# Sprawdzanie, czy plik istnieje
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename = input("Enter filename to read: ")

# Lista do przechowywania wczytanych adresów
webaddresses = []

# Otwieranie pliku w trybie odczytu i wczytywanie adresów stron
with open(filename, "r") as file:
    for line in file:
        webaddresses.append(line.replace("\n", ""))

# Pobranie katalogu, w którym znajduje się plik wejściowy
dirname = os.path.dirname(filename)

# Ścieżki dla dwóch nowych plików wynikowych
websPathPL = os.path.join(dirname, "webs_pl.txt")  # Plik z polskimi adresami
websPathOther = os.path.join(dirname, "webs_other.txt")  # Plik z innymi adresami

# Otwieranie plików wynikowych w trybie zapisu
filePL = open(websPathPL, "w")
fileOther = open(websPathOther, "w")

# Iterowanie przez adresy i zapisywanie ich w odpowiednich plikach
for line in webaddresses:
    if line.endswith(".pl"):  # Adres kończy się na '.pl'
        filePL.write(line + "\n")
    else:  # Wszystkie inne adresy
        fileOther.write(line + "\n")

# Zamknięcie plików wynikowych
filePL.close()
fileOther.close()
