# Generator zwracający kolejne potęgi liczby 2 (yield w pętli while).
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2**n
        n += 1


a = PowTwoGen(100)
for i in range(100):
    print(next(a))
