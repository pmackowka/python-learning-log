# lambda jako odpowiednik zwykłej funkcji, z filter() i jako wynik funkcji zwracającej funkcję (closure).
def double(x):
    return x * 10


result = double(10)
print(result)

f = lambda x: x * 10
print(f(10))

print("-" * 20)


def power(x, y):
    return x**y


x = 5
y = 3
print(power(x, y))

f = lambda x, y: x**y
print(f(5, 3))

print("-" * 20)

list_numbers = [1, 2, 3, 4, 11, 14, 15, 20, 21]

f = filter(lambda x: x % 2 != 0, list_numbers)
print(list(f))
# [1, 3, 11, 15, 21]

print("-" * 20)


def generate_multiply_function(n):
    return lambda x: x * n


num_2 = generate_multiply_function(2)
num_3 = generate_multiply_function(3)

print(num_2(10), num_3(20))
# 20 60
