# Jak main-1.py, z dodanymi komentarzami wyjaśniającymi każdy krok.
import pandas as pd  # Importowanie biblioteki Pandas do analizy i przetwarzania danych
from matplotlib import (
    pyplot as plt,  # Importowanie funkcji do tworzenia wykresów z biblioteki Matplotlib
)

# Wczytanie danych z pliku Parquet do DataFrame Pandas
taxi = pd.read_parquet(
    "./datasets/yellow_tripdata_2021-05.parquet",  # Ścieżka do pliku danych
    engine="auto",  # Automatyczny wybór silnika do odczytu pliku Parquet
    columns=None,  # Wczytanie wszystkich kolumn (brak selekcji)
    storage_options=None,  # Brak dodatkowych opcji przechowywania
    use_nullable_dtypes=False,  # Użycie standardowych typów danych zamiast nullable
)

print("-" * 10)
# Wyświetlenie liczby niepustych wartości w każdej kolumnie DataFrame
print(taxi.count())

print("-" * 10)
# Wyświetlenie pierwszych 5 wierszy DataFrame
print(taxi.head())

# Separator dla czytelności
print("-" * 10)
# Wyświetlenie szczegółowych informacji o DataFrame, takich jak typy kolumn i użycie pamięci
print(taxi.info())

# Separator dla czytelności
print("-" * 10)
# Wyświetlenie statystyk opisowych dla kolumn liczbowych w DataFrame
print(taxi.describe())

# Inicjalizacja pustej listy do przechowywania średnich odległości z próbek
means = []
# Pętla iterująca przez 100 różnych wartości ułamka (od 0% do 99%)
for f in range(100):
    # Tworzenie losowej próbki danych o wielkości stanowiącej 'f%' oryginalnego zbioru
    df_probe = taxi.sample(frac=f / 100)
    # Obliczenie średniej odległości (kolumna 'trip_distance') w tej próbce
    probe_mean = df_probe["trip_distance"].mean()
    # Dodanie średniej z próbki do listy
    means.append(probe_mean)
    # Wyświetlenie aktualnej wartości ułamka i obliczonej średniej
    print(f, probe_mean)

# Tworzenie wykresu średnich z próbek
plt.plot(means)  # Linie łączące średnie z każdej iteracji
# Dodanie poziomej linii reprezentującej średnią z całego zbioru danych
plt.hlines(
    xmin=0,  # Początek linii na osi X
    xmax=100,  # Koniec linii na osi X
    y=taxi["trip_distance"].mean(),  # Wartość Y reprezentująca globalną średnią
    linestyles="solid",  # Styl linii - pełna
    colors="red",  # Kolor linii - czerwony
)
# Wyświetlenie wykresu
plt.show()
