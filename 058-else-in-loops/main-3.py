"""LAB - Polecenie else w pętlach
W tym zadaniu należy zapisać na dysku zawartość kilku stron www. Po zakończeniu pobierania należy wyświetlić komunikat o powodzeniu. Jednak w przypadku błędu należy wyświetlić informację o błędzie i przerwać pętlę. Jeśli taki opis Ci wystarcza - do działa!

A oto opis "krok po kroku"
zaimportuj moduły os i urllib.request
w zmiennej data_dir zapisz ścieżkę do katalogu, w którym mają być zapisywane strony
w zmiennej pages zapisz informacje o stronach do pobrania. Może to być np. lista słowników:
pages = [
    {'name': 'google cloud', 'url': 'https://cloud.google.com/gcp'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},  # Strona nie istnieje
    {'name': 'microsoft azure', 'url': 'https://azure.microsoft.com/pl-pl'}
]

dla każdej stony z pages:
zapisz w zmiennej path ścieżkę do pliku powstałą z połączenia data_dir, nazwy strony pobranej z  pages i ".html"
korzystając z  funkcji urllib.request.urlretrieve(<adres strony>, <sciezka do pliku>) zapisz stronę na dysku
(na tym etapie przetestuj sobie działanie programu)
wewnątrz pętli for dodaj blok try/except, który w przypadku błędu zakończy wykonywanie pętli, wyświetlając komunikat o błędzie
zakończ pętlę for poleceniem, które wykona się tylko wtedy gdy pętla nie została w żaden sposób przerwana. Wyświetl tu komunikat o powodzeniu"""

import os  # Import modułu do operacji na systemie plików
import tempfile  # Katalog tymczasowy - pobrane strony nie trafiają do repo
import urllib.request  # Import modułu do pobierania stron www

# Ścieżka do katalogu, gdzie będą zapisywane pobrane strony
data_dir = tempfile.gettempdir()

# Lista stron do pobrania
pages = [
    {"name": "google cloud", "url": "https://cloud.google.com/gcp"},
    {"name": "nonexistent", "url": "http://abc.cde.fgh.ijk.pl/"},  # Strona nie istnieje
    {"name": "microsoft azure", "url": "https://azure.microsoft.com/pl-pl"},
]

# Iterujemy przez listę stron
for page in pages:
    try:
        # Tworzymy ścieżkę do pliku wynikowego
        path = os.path.join(data_dir, f"{page['name']}.html")

        # Pobieramy stronę i zapisujemy ją w określonej ścieżce
        urllib.request.urlretrieve(page["url"], path)
        print(f"Strona {page['name']} została zapisana jako {path}")
    except Exception as e:  # Obsługa błędów
        print(f"Błąd podczas pobierania strony {page['name']}: {e}")
        break  # Przerywamy pętlę w przypadku błędu
else:
    # Wykonuje się tylko, gdy pętla zakończyła się bez przerwań
    print("Wszystkie strony zostały pomyślnie pobrane!")
