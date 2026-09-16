# Napisz generator x, który zwróci 10 kolejnych wielokrotności liczby 5 - zaczynając od 5, kończąc na 50 (włącznie).
# Następnie napisz pętlę for, która wypisze kolejne wartości zwracane przez generator (i nie spowoduje wypisania StopIteration Error).

generator = (x for x in range(5, 51, 5))

for i in range(10):
    print(next(generator))

x = (n * 5 for n in range(1, 11))

for _ in range(10):
    print(next(x))

# L = [x ** 5 for x in range(5, 51, 5)]
# print(L)
