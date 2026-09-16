r"""LAB - Specjalne argumenty - args i kwargs
ZADANIE 1

Przygotowujesz program dla sklepu z farbami. Klienci pytają czasami ile farby potrzeba do pomalowania mieszkania.
Napisz funkcję calculate_paint, która:
przyjmuje argument efficency_ltr_per_m2 - określającą ile farby trzeba do pomalowania metra kwadratowego
przyjmuje dowolną ilość kolejnych argumentów odpowiadających za powierzchnie do pomalowania dla pokoi mieszkania, które ma być pomalowane funkcja ma zwracać informację o ilości potrzebnej farby

Przetestuj funkcję na dwa sposoby:
przekazując powierzchnie do pomalowania w poszczególnych pokojach po prostu po przecinku wywołując funkcję
definiując listę z powierzchniami, a następnie przekazując do funkcji tą listę

ZADANIE 2

Piszesz funkcję log_it, która ma zapisać w pliku tekstowym np. c:\temp\log_it.txt przesłane do funkcji argumenty. Funkcja będzie wykorzystywana w innych miejscach programu, gdzie będzie wywoływana w strategicznych momentach, dokumentując działanie programu. Jeśli nie masz innych pomysłów to zadbaj o to aby:

można było przesłać dowolną ilość argumentów

podczas dopisywania informacji do pliku poszczególne argumenty rozdzielaj spacją

na końcu w pliku zapisz ENTER, aby kolejne wywołanie funkcji dopisywało od nowej linijki

Przetestuj działanie funkcji wywołując ją np w taki sposób:"""

import tempfile
from pathlib import Path


def calculate_paint(efficiency_ltr_per_m2, *areas):
    total_area = sum(areas)
    paint_needed = total_area * efficiency_ltr_per_m2

    return paint_needed


efficiency = 0.1
paint_needed_test1 = calculate_paint(efficiency, 20, 15, 10, 25)
print(f"Test 1 - Potrzebna ilość farby: {paint_needed_test1:.2f} litrów")

areas = [20, 15, 10, 25]
paint_needed_test2 = calculate_paint(efficiency, *areas)
print(f"Test 2 - Potrzebna ilość farby: {paint_needed_test2:.2f} litrów")

print("-" * 30)


def calculate_paint(efficiency_ltr_per_m2, *areas):
    paint_per_room = [area * efficiency_ltr_per_m2 for area in areas]

    total_paint = sum(paint_per_room)

    return paint_per_room, total_paint


efficiency = 0.1
paint_per_room_test1, total_paint_test1 = calculate_paint(efficiency, 20, 15, 10, 25)
print(f"Test 1 - Farba na każdy pokój: {paint_per_room_test1}")
print(f"Test 1 - Łączna ilość farby: {total_paint_test1:.2f} litrów")

areas = [20, 15, 10, 25]
paint_per_room_test2, total_paint_test2 = calculate_paint(efficiency, *areas)
print(f"Test 2 - Farba na każdy pokój: {paint_per_room_test2}")
print(f"Test 2 - Łączna ilość farby: {total_paint_test2:.2f} litrów")


print("-" * 30)


def log_it(*args):
    log_file_path = Path(tempfile.gettempdir()) / "log-1.txt"

    # Wszystkie argumenty są konwertowane na ciąg znaków (str), co pozwala na obsługę różnych typów
    log_entry = " ".join(map(str, args)) + "\n"

    # Użyto trybu "a" (append), aby dopisywać dane do pliku bez nadpisywania istniejącej zawartości.
    with open(log_file_path, mode="a", encoding="utf-8") as file:
        file.write(log_entry)
        file.write("\n")


# Test funkcji
log_it("Starting processing forecasting")
log_it("ERROR", "Not enough data", "invoices", "2020")
