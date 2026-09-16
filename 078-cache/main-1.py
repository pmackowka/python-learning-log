# Rekurencyjna silnia z time.sleep() - baseline bez cache'owania (każde wywołanie jest wolne).
import time


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
# 5.719232082366943
