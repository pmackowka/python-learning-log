# Importowanie bibliotek do analizy danych i wizualizacji
import pandas as pd  # Główna biblioteka do analizy i manipulacji danych
from matplotlib import pyplot as plt  # Biblioteka do tworzenia wykresów
from matplotlib.ticker import (
    PercentFormatter,  # Formatter do osi wykresów, aby wyświetlać wartości w procentach
)
from pandas.api.types import (
    CategoricalDtype,  # Klasa do definiowania typów danych kategorycznych
)

# Wczytywanie danych z pliku w formacie Parquet (wydajny format dla dużych zbiorów danych)
taxi = pd.read_parquet(
    "./datasets/yellow_tripdata_2021-05.parquet",  # Ścieżka do pliku z danymi
    engine="auto",  # Automatyczny wybór silnika do odczytu plików Parquet
    columns=[
        "tpep_pickup_datetime"
    ],  # Wczytanie tylko kolumny z datą i godziną rozpoczęcia kursu
    storage_options=None,  # Domyślne opcje przechowywania
    use_nullable_dtypes=False,  # Nie używa typów nullable Pandas
)

# Filtrowanie danych do zakresu dat od 2 do 29 maja 2021 roku
taxi = taxi.query(
    "tpep_pickup_datetime >= '2021-05-02' and tpep_pickup_datetime < '2021-05-30'"
)

# Definiowanie kolejności dni tygodnia dla danych kategorycznych
cat_weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]  # Lista dni tygodnia
cat_type = CategoricalDtype(
    categories=cat_weekdays, ordered=True
)  # Definiowanie typu kategorycznego z określoną kolejnością

# Dodanie nowej kolumny z nazwą dnia tygodnia na podstawie daty w formacie kategorycznym
taxi["dayofweek"] = taxi["tpep_pickup_datetime"].dt.day_name().astype(cat_type)

# Grupowanie danych według dnia tygodnia i liczenie liczby wystąpień dla każdego dnia
taxi = taxi.groupby(["dayofweek"], as_index=False).count()

# Wyświetlenie tabeli zliczonych wartości
print(taxi)

# Zmiana nazwy kolumny na bardziej opisową
taxi.rename(
    columns={"tpep_pickup_datetime": "count"}, inplace=True
)  # Zmiana nazwy kolumny na 'count'

# Ponowne wyświetlenie przekształconych danych
print(taxi)

# Ustawienie 'dayofweek' jako indeksu danych, aby ułatwić dalszą analizę
taxi.set_index("dayofweek", inplace=True)

# Wyświetlenie tabeli z nowym indeksem
print(taxi)

# Tworzenie wykresu słupkowego liczby kursów dla każdego dnia tygodnia
taxi.plot.bar(y="count", legend=False)  # Wykres słupkowy, bez legendy
plt.show()  # Wyświetlenie wykresu

# Tworzenie wykresu kołowego z procentowym udziałem kursów dla każdego dnia
taxi.plot.pie(
    y="count",  # Kolumna do wizualizacji
    legend=False,  # Wyłączenie legendy
    counterclock=False,  # Wykres zgodny z ruchem wskazówek zegara
    autopct="%1.1f%%",  # Formatowanie wartości procentowych
)
# plt.ylabel("")  # Opcjonalne usunięcie etykiety osi
plt.show()  # Wyświetlenie wykresu

# --- Tworzenie wykresu Pareto (80/20) na podstawie dni tygodnia ---
# Sortowanie danych w porządku malejącym według liczby kursów
taxi.sort_values(by="count", ascending=False, inplace=True)

# Dodanie kolumny z procentowym skumulowanym udziałem liczby kursów
taxi["cummulative_percent"] = taxi["count"].cumsum() / taxi["count"].sum() * 100

# Wyświetlenie tabeli z dodaną kolumną
print(taxi)

# Tworzenie wykresu Pareto
fig, ax = plt.subplots()  # Utworzenie obiektu wykresu i osi
ax.bar(taxi.index, taxi["count"], color="C0")  # Wykres słupkowy liczby kursów
ax2 = ax.twinx()  # Tworzenie drugiej osi y (po prawej stronie)
ax2.plot(
    taxi.index, taxi["cummulative_percent"], color="C1", marker="D", ms=7
)  # Wykres liniowy skumulowanych procentów
ax2.yaxis.set_major_formatter(PercentFormatter())  # Formatowanie osi y w procentach

# Dostosowanie kolorów etykiet osi do koloru wykresów
ax.tick_params(axis="y", colors="C0")  # Kolor osi y po lewej stronie
ax2.tick_params(axis="y", colors="C1")  # Kolor osi y po prawej stronie

# Wyświetlenie wykresu Pareto
plt.show()
