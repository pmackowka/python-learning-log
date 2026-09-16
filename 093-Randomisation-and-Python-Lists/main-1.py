# random.randint() na dwa sposoby (pozycyjnie i przez a=/b=) oraz generowanie
# listy losowych liczb w pętli for i while.
import random

random.randint(1, 10)
random.randint(a=1, b=10)

a = [int(random.random() * 10) for _ in range(10)]
print(a)


# losowa_liczba = random.randint(1, 100)  # Losuje liczbę od 1 do 100
# print(losowa_liczba)


for _ in range(5):
    losowa_liczba = random.randint(1, 100)
    print(losowa_liczba)


count = 0
while count < 5:
    losowa_liczba = random.randint(1, 100)
    print(losowa_liczba)
    count += 1
