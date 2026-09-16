# Wypisz zawartość listy A dodając przed każdym elementem kolejny numer.
# Zacznij numerowanie od 0.

A = [1, 1, 4, 9]

num = 1
for element in A:
    print(num, element)
    num += 1

print("-" * 30)

for idx, element in enumerate(A, 1):
    print(idx, element)
