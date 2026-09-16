"""Jak main-2.py, ale sprawdzenie istnienia pliku i policzenie słów zapisane krócej."""

import os
from pathlib import Path


def CountWords(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        word_count = len(content.split())
    return word_count


path = Path(__file__).parent / "main-3-file-1.txt"

if os.path.isfile(path):
    print(f"There are {CountWords(path)} words in the file {path}")


os.path.isfile(path) and print(f"There are {CountWords(path)} words in the file {path}")
