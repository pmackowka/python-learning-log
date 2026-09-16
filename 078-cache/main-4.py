# lru_cache na rekurencyjnym fib() - liczenie Fibonacciego dla 34 pierwszych wartości.
import functools
import time


@functools.lru_cache(maxsize=100)
def fib(n):

    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()

for i in range(34):
    result = fib(i)
    print(f"{i:2d}  {result}, time = {time.time() - start:3.2f}")
# 8  21, time = 0.00

print(fib.cache_info())
