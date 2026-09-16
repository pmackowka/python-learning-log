# Stwórz klasę Kot, a w niej konstruktor, który będzie pobierał imie i kolor.
# Do zmiennej k przypisz obiekt klasy Kot, daj mu na imię "Mruczek" i dowolny kolor.
# Dalsza część kodu zajmie się wypisaniem imienia obiektu przechowywanego pod zmienną k.


class Kot:
    def __init__(self, imie, kolor):
        self.imie = imie
        self.kolor = kolor


k = Kot("Mruczek", "Szary")
print(k.imie)
