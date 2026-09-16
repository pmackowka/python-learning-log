"""LAB - Zagnieżdżanie pętli i to samo w postaci jednolinijkowej
Postanawiasz otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:"""

ports = [
    "WAW",
    "KRK",
    "GDN",
    "KTW",
    "WMI",
    "WRO",
    "POZ",
    "RZE",
    "SZZ",
    "LUZ",
    "BZG",
    "LCJ",
    "SZY",
    "IEG",
    "RDO",
]

"""1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym
2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu
3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A - wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.
4. Policz ilość generowanych połączeń w krokach 1,2,3"""

print("-" * 20)
airlines = []
for s in ports:
    for e in ports:
        airlines.append((s, e))
print(len(airlines))

print("-" * 20)
airlines = [(s, e) for s in ports for e in ports if not s == e]
print(len(airlines))

print("-" * 20)
airlines = [(start, end) for start, end in airlines if start != end]
print(len(airlines))

print("-" * 20)
# 3. Eliminacja zdublowanych połączeń, np. (A, B) i (B, A)
unique_connections = []
for start, end in airlines:
    if (
        end,
        start,
    ) not in unique_connections:  # Dodaj tylko jeśli odwrócone połączenie nie istnieje
        unique_connections.append((start, end))
print(len(unique_connections))
