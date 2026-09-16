# Funkcja jako argument (how) generująca listę wartości przez zastosowanie jej do x_table.
def double(x):
    return 2 * x


def square(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(how, x_table):
    value_list = []
    for x in x_table:
        value_list.append(how(x))  # double(0), double(1)

    return value_list  # [double(0), double(1)]


x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
# [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
