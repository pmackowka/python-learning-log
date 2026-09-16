# Silnia przez pętlę for (ręcznie i przez math.factorial) oraz zagnieżdżone pętle for
# (iloczyn kartezjański przymiotników i rzeczowników).
i = 10
result = 1

for j in range(1, i + 1):
    result *= j

print(i, result)
# 10 3628800

print("------------")

import math

print(10, math.factorial(10))
# 10 3628800

print("------------")

x = 10
for i in range(1, x + 1):
    result = 1

    for j in range(1, i + 1):
        result *= j

    print(i, result)
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120
# 6 720
# 7 5040
# 8 40320
# 9 362880
# 10 3628800

print("------------")

list_noun = ["dog", "potato", "meal", "icecream", "car"]
list_adj = ["dirty", "big", "hot", "colorful", "fast"]

for noun in list_noun:
    for adj in list_adj:
        print(adj, noun)
