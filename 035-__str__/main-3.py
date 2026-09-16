# Uzupełnij klasę Kot o metodę __str__, która po wydrukowaniu obiektu k wypisze "Kot Mruczek jest rudy".


class Kot:
    def __init__(self, imie, kolor):
        self.imie = imie
        self.kolor = kolor

    def __str__(self):
        return f"Kot {self.imie} jest {self.kolor}"


k = Kot("Mruczek", "rudy")

print(k)
