# Generator (wyrażenie generatorowe) zamiast listy - next() ręcznie, iteracja for, StopIteration.
listA = list(range(6))
listB = list(range(6))


product = [(a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
print(product)

print("-" * 20)
gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
print(next(gen))
print(next(gen))
print(next(gen))
print("-" * 20)

for g in gen:
    print(g)

print("-" * 20)
gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print("Wszystkie tuple zostały wygenerowane")
        break
