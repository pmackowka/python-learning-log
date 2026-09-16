# Jak main-3.py, ale bez process_transformations() - pętla wypisana wprost, na dwóch przykładach.
def double(x):
    return 2 * x


def square(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8
transformations = [double, square, div2, negative]

print("Starting transformations")
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print(f"{transformation.__name__}: temporal result is {tmp_return_value}")

# Starting transformations
# double: temporal result is 16
# square: temporal result is 256
# div2: temporal result is 128.0
# negative: temporal result is -128.0

number = 125
transformations = [square, square, div2, double]

print("Starting transformations")
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print(f"{transformation.__name__}: temporal result is {tmp_return_value}")

# Starting transformations
# square: temporal result is 15625
# square: temporal result is 244140625
# div2: temporal result is 122070312.5
# double: temporal result is 244140625.0
