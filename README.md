# python-learning-log

Dziennik nauki Pythona - nie projekt produkcyjny, nie portfolio w sensie "gotowej aplikacji".
Zbiór ćwiczeń w kolejności, w jakiej powstawały: od list i słowników, przez pętle, funkcje,
dekoratory i generatory, po podstawy programowania obiektowego i analizę danych w pandas.

Część zadań ma formę pytań ("Pytanie N - ...") z krótkim rozwiązaniem, część to dłuższe
skrypty rozwijane w kilku wariantach (`main-1.py`, `main-2.py`, ...) w tym samym folderze.

## Struktura

Każdy folder to jedno ćwiczenie, numerowane w kolejności powstawania:

```
048-while-loop/
├── main-1.py
├── main-2.py
└── ...
```

Warianty `main-N.py` w tym samym folderze zwykle rozwijają to samo zadanie krok po kroku
(np. najpierw wersja bez obsługi błędów, potem z obsługą) - każdy plik ma na górze
jednozdaniowy komentarz opisujący, co pokazuje i czym różni się od poprzedniego wariantu.

| Zakres | Temat |
|---|---|
| 001-047 | Podstawy w formie pytań: listy, słowniki, slice'owanie, comprehensions, lambda, dekoratory, generatory, pierwsze starcie z OOP, rekurencja, złożoność (Big-O), PEP8 |
| 048-072 | Pętle, funkcje, wejście/wyjście, obsługa błędów, typy, instrukcje warunkowe, `eval`/`exec`/`compile`, `*args`/`**kwargs`, funkcje jako obiekty |
| 073-079 | Biblioteki zewnętrzne, dekoratory z parametrem, wysyłka maila przez SMTP, `functools.partial`, cache, lambda |
| 080-089 | OOP: klasy, atrybuty instancji i klasy, metody, `@property`, iteratory (`__iter__`/`__next__`) |
| 090-091 | Analiza danych i wykresy (pandas, matplotlib) |
| 092-095 | Drugi przegląd podstaw - instrukcje warunkowe, losowość, pętle, funkcje; mini-projekty (Hangman, kamień-papier-nożyce) |

## Uruchamianie

```bash
python3 -m pip install -r requirements.txt
python3 048-while-loop/main-1.py
```

Wymaga Pythona 3.11+. Część skryptów pyta o dane przez `input()` - trzeba je odpalać
w terminalu, nie da się ich po prostu "zaimportować".

**Wyjątek:** `090-statistics-probe-population` i `091-statistics-data-types-charts` odwołują
się do zewnętrznego pliku `datasets/yellow_tripdata_2021-05.parquet` (NYC TLC Yellow Taxi
Trip Data), którego nie ma w repo - trzeba go pobrać samodzielnie, żeby te dwa ćwiczenia
zadziałały.

## Uwaga o jakości kodu

To jest zapis nauki, nie kod produkcyjny. Część plików celowo pokazuje "zły" wzorzec, żeby
go potem wyjaśnić - np. mutowalny argument domyślny (`019-default-arguments`), różnicę
między `is` a `==` (`020-is-versus-==`, `021-chain-comparisons`) czy ryzyko `eval()`/`exec()`
na niezaufanym wejściu (`064-eval`, `065-exec`, `066-compile`). Te fragmenty są nietknięte
celowo - nie traktuj ich jako rekomendowanego stylu do kopiowania.

Konwencja w kodzie: nazwy i identyfikatory po angielsku, komentarze po polsku (część
wcześniejszych ćwiczeń miesza oba języki - to ślad tego, jak faktycznie wyglądała nauka).
