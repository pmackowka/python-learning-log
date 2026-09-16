"""LAB - Funkcja jako argument funkcji
Dane są następujące funkcje:"""


def double(x):
    return 2 * x


def square(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x / 2


"""Napisz funkcję, która stanie się wspólnym interfejsem dla tych funkcji. Niech nowa funkcja nazywa sie generate_values i:
jako pierwszy argument przyjmuje nazwę funkcji (jedną z wyżej wymienionych)
jako drugi argument przyjmuje listę liczb, dla których ma być wyznaczona wartość
ta funkcja powinna wygenerować wartość dla każdej wartości z listy z poprzedniego punktu i zwrócić listę z wynikami
Przetestuj funkcję wywołując:"""


def generate_values(name_functions, numbers):
    # Zwraca nową listę, gdzie każda liczba została przetworzona przez funkcję name_fun
    return [name_functions(num) for num in numbers]


# Testowanie funkcji generate_values
x_table = list(range(11))

print(generate_values(double, x_table))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(generate_values(square, x_table))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(
    generate_values(negative, x_table)
)  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
print(
    generate_values(div2, x_table)
)  # [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
