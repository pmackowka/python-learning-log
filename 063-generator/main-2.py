"""LAB - Generatory
W tym zadaniu należy przerobić listy z poprzedniego LAB do postaci generatora.  Nieco problematyczne będzie ustalenie ile wartości jest generowanych przez generator, bo w tym celu... trzeba go przejść!

Jeżeli taki opis Ci wystarcza to GO! GO! GO!

A tu dokładniejsza instrukcja:
Postanawiasz wraz ze swoim szefem otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:"""

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


print("-" * 30)
gen_routes = ((start, stop) for start in ports for stop in ports)
while True:
    try:
        print(next(gen_routes))
    except StopIteration:
        print("Zakończenie generatora")
        break

print("-" * 30)
gen_routes = ((start, stop) for start in ports for stop in ports)
for routes in gen_routes:
    print(routes)

print("-" * 30)
gen_routes = ((start, stop) for start in ports for stop in ports if start != stop)
while True:
    try:
        print(next(gen_routes))
    except StopIteration:
        print("Zakończenie generatora")
        break


print("-" * 30)
gen_routes = ((start, stop) for start in ports for stop in ports if start < stop)
print(gen_routes)  # <generator object <genexpr> at 0x1050b7890>

print("-" * 30)
while True:
    try:
        print(next(gen_routes))
    except StopIteration:
        print("Zakończenie generatora")
        break
