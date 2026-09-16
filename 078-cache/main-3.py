"""LAB - Optymalizacja funkcji przez cache
Oto przykład niezbyt dobrze napisanej funkcji wyliczającej wartość w ciągu Finobacciego:"""

import time
from functools import lru_cache


# Funkcja pierwotna, nieoptymalna
def fib_original(n):
    if n < 2:
        return n
    return fib_original(n - 1) + fib_original(n - 2)


# Zoptymalizowana funkcja z wykorzystaniem lru_cache
@lru_cache(maxsize=100)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


# Test pomiaru czasu
def measure_execution_time(func, max_iterations):
    start = time.time()
    for i in range(1, max_iterations + 1):
        result = func(i)
        elapsed = time.time() - start
        print(f"Iteration {i}: Time elapsed: {elapsed:.6f} seconds")
    total_time = time.time() - start
    print(f"Total time: {total_time:.6f} seconds")
    return total_time


print("Testing original function...")
try:
    time_original = measure_execution_time(fib_original, 33)
except RecursionError:
    print("RecursionError: zbyt duża wartość n dla funkcji oryginalnej!")

print("\nTesting cached function...")
time_cached = measure_execution_time(fib_cached, 33)

print("\nCache info for optimized function:")
print(fib_cached.cache_info())
