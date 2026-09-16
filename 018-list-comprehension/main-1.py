# Pytanie 20 - co otrzymamy w wyniku wydrukowania zawartości poniższych zmiennych?

L = [1, 2, 3, 4, 5, 6]

L1 = [x for x in range(5)]  # wpisz do listy L1 elementy z zakresu od 0 do 4
L2 = [x**2 for x in L]  # wpisz do listy L2 elementy z listy L podniesione do kwadratu
L3 = [
    x for x in L if x % 2 == 0
]  # wpisz do listy L3 elementy z listy L, tylko jeśli dany element jest podzielny przez 2
L4 = ["Parzysta" if x % 2 == 0 else "Nieparzysta" for x in range(5)]
# wpisz do listy L4 'Parzysta' lub 'Nieparzysta' w zależności od tego czy kolejny element
# z zakresu 0 do 4 jest podzielny lub nie jest podzielny przez 2
L5 = [
    (x, x + 10) for x in L
]  # wpisz do listy L5 dwuelementowe tuple, które na indeksie 0 mają kolejny element z lsty L
# a na indeksie 1 ten sam element zwiększony o 10
D1 = {
    x: x % 2 == 0 for x in L
}  # wpisz do słownika D1 pary klucz:wartość, gdzie kluczem są elementy z listy L
# a wartościami True lub False, w zależności od tego czy dany klucz jest podzielny przez 2

print(L1)  # [0, 1, 2, 3, 4]
print(L2)  # [1, 4, 9, 16, 25, 36]
print(L3)  # [2, 4, 6]
print(L4)  # ['Parzysta', 'Nieparzysta', 'Parzysta', 'Nieparzysta', 'Parzysta']
print(L5)  # [(1, 11), (2, 12), (3, 13), (4, 14), (5, 15), (6, 16)]
print(D1)  # {1: False, 2: True, 3: False, 4: True, 5: False, 6: True}
