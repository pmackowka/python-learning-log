# Iloczyn kartezjański dwóch list - zagnieżdżona pętla for, list/dict comprehension, warunki.
listA = list(range(6))
listB = list(range(6))

print(listA, listB)

print("-" * 20)

product = []
for a in listA:
    for b in listB:
        product.append((a, b))
print(product)

print("-" * 20)
product = [(a, b) for a in listA for b in listB]
print(product)

print("-" * 20)
product = [(a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
print(product)

print("-" * 20)
product = {a: b for a in listA for b in listB if a % 2 == 1 and b % 2 == 0}
print(product)

print("-" * 20)
tie = ["green tie", "gray tie", "red tie"]
shirt = ["white shirt", "blue shirt", "green shirt"]
print([f"I wear {t} with {s}" for t in tie for s in shirt])

print("-" * 20)
clients = ["A-company", "B-company"]
projects = [300, 400, 1500, 2340, 50]
investments = [
    (c, p)
    for c in clients
    for p in projects
    if c == "A-company" and p < 1000 or c == "B-company" and p >= 1000
]
print(investments)
