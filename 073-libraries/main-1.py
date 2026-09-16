"""Przegląd popularnych bibliotek standardowych i zewnętrznych Pythona.

Uwaga: plik ma charakter poglądowy (katalog przykładów), nie skryptu do jednorazowego
uruchomienia - część fragmentów ma efekty uboczne (żądania HTTP, otwarcie przeglądarki
przez selenium) i wymaga zainstalowanych zależności z requirements.txt.
"""

import numpy as np

arr = np.array([1, 2, 3])
print(arr.mean())  # Wynik: 2.0

import pandas as pd

df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
print(df.describe())

# requests: HTTP API i pobieranie danych z internetu
import requests

response = requests.get("https://example.com")
print(response.text)

# selenium: Automatyzacja przeglądarek internetowych
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# bs4: Web scraping
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all("h1")
for title in titles:
    print(title.text)

# datetime: Standardowa biblioteka do manipulacji datami i czasem
from datetime import datetime

now = datetime.now()
print(now)

# time:


# timedelta: Zawiera funkcje pomocnicze do obliczania różnicy między datami (czas, dni, godziny, minuty)
from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=5)
print(future)


# pytest: Testy jednostkowe, funkcyjne i integracyjne
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


# typing: Statyczne typowanie
# Moduł standardowy w Pythonie, służący do dodawania adnotacji typów w kodzie.


def add_numbers(numbers: list[int]) -> int:
    return sum(numbers)


print(add_numbers([1, 2, 3]))  # Poprawne
# print(add_numbers(["a", "b"]))  # Błąd wykrywany przez narzędzia analizy statycznej


# mypy: Statyczne typowanie
# Narzędzie zewnętrzne do analizy statycznej kodu Pythona. Wykorzystuje adnotacje typów (dodane np. za pomocą modułu typing) i sprawdza, czy kod jest zgodny z zadeklarowanymi typami.
def greet(name: str) -> str:
    return f"Hello, {name}!"


greet(123)  # Błąd typowania

# os: zapewnia funkcje do interakcji z systemem operacyjnym
import os
from pathlib import Path

sample_dir = (
    Path(__file__).parent.parent
    / "040-recursively-listing-the-contents-of-a-directory"
    / "sample_dir"
)
print(os.listdir(sample_dir))
# ['b.txt', 'a.txt', 'nested']

# random: Generowanie liczb losowych
import random

# Liczba zmiennoprzecinkowa z zakresu [0.0, 1.0)
print(random.random())
# Liczba całkowita z zakresu [10, 20]
print(random.randint(10, 20))
# Liczba zmiennoprzecinkowa z zakresu [10.5, 20.5]
print(random.uniform(10.5, 20.5))

# functools: Moduł functools w Pythonie zawiera narzędzia do pracy z funkcjami i metodami

# pickle: Umożliwia serializację (zapis) i deserializację (odczyt) obiektów Python do/z plików binarnych

# glob: Umożliwia wyszukiwanie plików i katalogów pasujących do określonego wzorca (ang. pattern matching).
