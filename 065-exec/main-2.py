"""LAB - Funkcja exec()
Tym razem pracujesz w zwariowanym ośrodku badawczym...

Profesorowie przygotowują swoje skrypty i umieszczają je w określonym katalogu. Kolejno:
main-3.py
main-4.py

Twój skrypt ma za zadanie przeczytać te skrypty i je po kolei wykonywać.

Poniżej znajdują się dwa przykładowe skrypty. Każdy z nich skopiuj i zapisz w osobnym pliku (jeżeli wykonanie skryptu miało by być zbyt długie, możesz zmienić ilość iteracji w zmiennej for, ale nie powinno być tak źle):
"""

import os
from pathlib import Path

# os.path.basename

BASE_DIR = Path(__file__).parent
files_to_process = [
    BASE_DIR / "main-3.py",
    BASE_DIR / "main-4.py",
]

for file in files_to_process:
    print(f"Procesujesz plik o nazwie: {os.path.basename(file)}")

    with open(file, "r") as f:
        source = f.read()

        exec(source)
        print(f"Zakończenie procesowania dla pliku: {os.path.basename(file)}\n\n")

# Procesujesz plik o nazwie: main-3.py
# min = 0.0  max = 9997170253.720783
# Zakończenie procesowania dla pliku: main-3.py


# Procesujesz plik o nazwie: main-4.py
# min = 0.0  max = 999997000002683.6
# Zakończenie procesowania dla pliku: main-4.py
