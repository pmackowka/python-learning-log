# random.random(), random.uniform(), random.randint() - symulacja rzutu monetą,
# modulo, krotka vs porównanie.
import random

number_a = random.random() * 10
print(number_a)

number_float = random.uniform(0, 2)
print(number_float)


l = random.randint(a=1, b=2)
if l == 1:
    print(f"Wylosowano {l} -> orzeł")
else:
    print(f"Wylosowano {l} -> reszka")


print(1 % 3)  # 1
print(2 % 3)  # 2
print(3 % 3)  # 0
print(4 % 3)  # 1
print(5 % 3)  # 2

result = 1, 2  # Tuple
print(result)

print(result == (1, 2))  # True
