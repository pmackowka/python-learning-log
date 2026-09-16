# Lista transformacji (funkcji) aplikowanych po kolei do liczby, z wypisywaniem wyniku każdego kroku.
def double(x):
    return 2 * x


def square(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8

transformations1 = [double, square, div2, negative]
transformations2 = [square, square, div2, double]


def process_transformations(number, transformations):
    tmp_return_value = number

    for transformation in transformations:
        tmp_return_value = transformation(tmp_return_value)
        print(f"After {transformation.__name__}: {tmp_return_value}")

    return tmp_return_value


print("Transformations 1:")
process_transformations(number, transformations1)

print("\nTransformations 2:")
process_transformations(number, transformations2)
