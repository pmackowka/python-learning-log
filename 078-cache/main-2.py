# Jak main-1.py, ale z @functools.lru_cache - drastyczne przyspieszenie dzięki cache'owaniu wyników.
import functools
import time


@functools.lru_cache
def Factorial(n):

    time.sleep(0.1)

    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


start = time.time()
for i in range(1, 11):
    print(f"{i}! = {Factorial(i)}")

stop = time.time()

print("Czas:", stop - start)

print(Factorial.cache_info())
# CacheInfo(hits=9, misses=10, maxsize=128, currsize=10)

# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
# 7! = 5040
# 8! = 40320
# 9! = 362880
# 10! = 3628800
# Czas: 1.0323688983917236
