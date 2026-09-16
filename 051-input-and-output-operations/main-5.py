# input() w pętli do zbierania adresów www, potem zapis listy do pliku.
import os

webaddresses = []
line = input('Enter web address like "www.python.org" or press ENTER to stop: ')

# Pętla do wprowadzania adresów
while line != "":
    webaddresses.append(line)  # Dodaj adres do listy
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')

print(webaddresses)  # Wyświetlenie listy wprowadzonych adresów

dirname = os.getcwd()  # Pobranie aktualnego katalogu roboczego
filename = input("Enter the file name (without directory): ")
filepath = os.path.join(dirname, filename)  # Utworzenie pełnej ścieżki do pliku

# Otwieranie pliku w trybie zapisu z możliwością odczytu (w+)
file = open(filepath, "w+")
file.writelines(
    webaddress + "\n" for webaddress in webaddresses
)  # Zapis adresów do pliku
file.close()  # Zamknięcie pliku
