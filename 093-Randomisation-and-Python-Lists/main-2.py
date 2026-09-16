# random.randint() oraz import lokalnego modułu (module_1) z gotową listą losowych liczb.
import random

import module_1

a = random.randint(a=1, b=10)
print(a)

b = random.randint(1, 10)
print(b)

print(module_1.c)
