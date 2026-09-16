"""Pobieranie kilku stron www z użyciem pętli for/else - powodzenie wypisywane
tylko wtedy, gdy pętla przeszła przez wszystkie strony bez przerwania (break)."""

import os
import tempfile
import urllib.request

# Katalog tymczasowy (poza repo, żeby pobrane strony nie zaśmiecały historii gita)
data_dir = tempfile.gettempdir()

# Lista stron do pobrania
pages = [
    {"name": "frisco", "url": "https://www.frisco.pl/"},
    {"name": "nonexistent", "url": "http://abc.cde.fgh.ijk.pl/"},  # Strona nie istnieje
    {"name": "microsoft_azure", "url": "https://azure.microsoft.com/pl-pl"},
]

# Pobieranie stron
for page in pages:
    try:
        # Tworzenie ścieżki do zapisu pliku
        file_name = f"{page['name']}.html"
        path = os.path.join(data_dir, file_name)

        # Informacja o przetwarzanej stronie
        print("Processing: ", page["url"], "=>", file_name, "...")
        urllib.request.urlretrieve(
            page["url"], path
        )  # Pobranie strony i zapis do pliku
        print("...done")  # Sukces

    except Exception as e:  # Obsługa błędów
        print("FAILURE processing web page: ", page["name"])
        print("Error: ", e)  # Wyświetlenie szczegółowego błędu
        print("Stopping the process!")
        break  # Przerwanie pętli w przypadku błędu

# Wykonanie, jeśli pętla nie została przerwana
else:
    print("All pages downloaded successfully!!!")

# Processing: https://www.frisco.pl/  => frisco.html ...
# ...done
# Processing: http://abc.cde.fgh.ijk.pl/  => nonexistent.html ...
# FAILURE processing web page: nonexistent
# Error: HTTP Error 404: Not Found
# Stopping the process!
