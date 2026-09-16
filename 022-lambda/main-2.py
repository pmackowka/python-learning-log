# Posortuj podaną listę stringów jako kryterium sortowania przyjmując ostatnią literę każdego stringa.

S = ["Anna", "Robert", "Artur", "Feliks"]

S_posortowana = sorted(S, key=lambda x: x[-1:])
print(S_posortowana)
# ['Anna', 'Artur', 'Feliks', 'Robert']

print(S[::-1])  # Lista odwrócona
# ['Feliks', 'Artur', 'Robert', 'Anna']
