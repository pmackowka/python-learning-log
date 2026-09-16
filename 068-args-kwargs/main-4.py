"""Jak main-2.py (ZADANIE 1 i 2), ale calculate_paint zwraca sumę, a log_it pisze linie ręcznie (bez join)."""

import tempfile
from pathlib import Path


def calculate_paint(efficency_ltr_per_m2, *rooms):
    total_area = sum(rooms)
    paint = total_area * efficency_ltr_per_m2
    return paint


print(calculate_paint(0.25, 42, 28, 30))

rooms = [42, 28, 30]
print(calculate_paint(0.25, *rooms))

print("-" * 30)


def log_it(*args):
    path = Path(tempfile.gettempdir()) / "log-2.txt"
    with open(path, "a") as f:
        for line in args:
            f.write(line)
            f.write(" ")

        f.write("\n")


log_it("Starting processing forecasting")
log_it("ERROR", "Not enough data", "invoices", "2020")
