"""Sprawdzenie/utworzenie folderu docelowego dla pliku (os.makedirs, os.path.exists)."""

import os
from pathlib import Path

file_path = Path(__file__).parent / "dummy_file.txt"

# Tworzenie folderów, jeśli nie istnieją
os.makedirs(file_path.parent, exist_ok=True)

# Weryfikacja
if os.path.exists(file_path.parent):
    print("Folder został pomyślnie utworzony lub już istnieje.")
else:
    print("Nie udało się utworzyć folderu.")

print(file_path.parent)
