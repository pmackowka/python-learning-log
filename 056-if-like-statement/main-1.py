"""Sprawdzenie, czy plik istnieje (os.path.isfile) i utworzenie go w trybie 'x', jeśli nie."""

import os  # Import modułu os do pracy z plikami i ścieżkami
from pathlib import Path

# Ścieżka do pliku
path = Path(__file__).parent / "main-1-file-1.txt"

# os.remove(path)

# Sprawdzanie, czy plik istnieje w podanej ścieżce
if os.path.isfile(path):
    print(
        "Plik pod ścieżką %s istnieje!" % path
    )  # Jeśli plik istnieje, wypisz komunikat
else:
    print(
        "Tworzenie pliku pod ścieżką %s" % path
    )  # Jeśli plik nie istnieje, wyświetl komunikat
    try:
        # Tworzenie pustego pliku w podanej ścieżce
        open(
            path, "x"
        ).close()  # 'w' oznacza tryb zapisu, który utworzy plik, jeśli nie istnieje
        print("Plik został utworzony %s" % path)  # Komunikat o utworzeniu pliku
    except FileExistsError as e:
        # Obsługa wyjątku, jeśli wystąpi błąd podczas tworzenia pliku
        print(f"Nie udało się utworzyć pliku: {e}")

"""
Podstawowe tryby:

	1.	'r' (read):
	•	Otwiera plik tylko do odczytu (domyślny tryb).
	•	Plik musi istnieć, w przeciwnym razie wyrzuci wyjątek FileNotFoundError.
	2.	'w' (write):
	•	Otwiera plik do zapisu.
	•	Jeśli plik istnieje, jego zawartość zostanie nadpisana.
	•	Jeśli plik nie istnieje, zostanie utworzony.
	3.	'x' (exclusive creation):
	•	Tworzy nowy plik, ale wyrzuca wyjątek FileExistsError, jeśli plik już istnieje.
	4.	'a' (append):
	•	Otwiera plik do dopisywania na końcu.
	•	Jeśli plik nie istnieje, zostanie utworzony.
	•	Zawartość istniejąca w pliku nie jest nadpisywana."""
