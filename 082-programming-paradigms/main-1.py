# 1. Programowanie proceduralne
# Skupia się na podziale programu na funkcje i instrukcje wykonywane sekwencyjnie.
def calculate_area(length, width):
    return length * width


def display_area(length, width):
    area = calculate_area(length, width)
    print(f"Pole prostokąta o wymiarach {length}x{width} wynosi {area}.")


length = 5
width = 3
display_area(length, width)
# Pole prostokąta o wymiarach 5x3 wynosi 15.


# 2. Programowanie obiektowe (OOP)
# Organizuje kod wokół obiektów, które łączą dane (atrybuty) i zachowania (metody).
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rect = Rectangle(5, 3)
print(rect.area())
# 15


# 3. Programowanie funkcjonalne (FP)
# Oparte na czystych funkcjach, niemutowalnych danych i funkcjach wyższego rzędu.
# Funkcjonalne: użycie map i lambda do przetwarzania danych
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  # Każda liczba podniesiona do kwadratu
print(squared)  # Wynik: [1, 4, 9, 16]


# 4. Programowanie imperatywne
# Skupia się na opisywaniu kroków wymaganych do osiągnięcia celu.
# Imperatywne: iteracja przez listę i modyfikacja jej elementów
numbers = [1, 2, 3, 4]
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
print(numbers)  # Wynik: [1, 4, 9, 16]


# 5. Programowanie deklaratywne
# Opisuje co ma zostać zrobione, a nie jak to zrobić. W Pythonie często wykorzystuje SQL lub biblioteki, jak pandas.
# Deklaratywne: filtrowanie liczb parzystych
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # Wynik: [2, 4, 6]


# 6. Programowanie asynchroniczne
# Służy do wykonywania operacji niezależnych od siebie w sposób współbieżny.
import asyncio


# Asynchroniczne: wykonanie dwóch zadań jednocześnie
async def say_hello():
    await asyncio.sleep(1)
    print("Hello")


async def say_world():
    await asyncio.sleep(1)
    print("World")


async def main():
    await asyncio.gather(say_hello(), say_world())


asyncio.run(main())
# Wynik: "Hello" i "World" pojawiają się niemal jednocześnie
