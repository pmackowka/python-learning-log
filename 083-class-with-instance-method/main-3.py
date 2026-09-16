# Klasa Ciasto z metodami instancji (pokaz_informacje, ustaw_nadzienie, dodaj_dodatki).
class Ciasto:
    def __init__(self, nazwa, rodzaj, smak, dodatki, nadzienie):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.smak = smak
        self.dodatki = dodatki.copy()
        self.nadzienie = nadzienie

    def pokaz_informacje(self):
        print(f"{self.nazwa.upper()}")
        print(f"Rodzaj:  {self.rodzaj}")
        print(f"Smak:    {self.smak}")
        if len(self.dodatki) > 0:
            print("Dodatki:")
            for dodatek in self.dodatki:
                print(f"\t{dodatek}")
        if len(self.nadzienie) > 0:
            print(f"Nadzienie: {self.nadzienie}")
        print("-" * 20)

    def ustaw_nadzienie(self, nadzienie):
        self.nadzienie = nadzienie

    def dodaj_dodatki(self, nowe_dodatki):
        self.dodatki.extend(nowe_dodatki)


ciasto_1 = Ciasto(
    "Ciasto Waniliowe", "ciasto", "waniliowe", ["czekolada", "orzechy"], "krem"
)
ciasto_2 = Ciasto("Muffinka Czekoladowa", "muffinka", "czekoladowy", ["czekolada"], "")
ciasto_3 = Ciasto("Beza Super Słodka", "beza", "bardzo słodki", [], "")

oferta_cukierni = []
oferta_cukierni.append(ciasto_1)
oferta_cukierni.append(ciasto_2)
oferta_cukierni.append(ciasto_3)

ciasto_2.ustaw_nadzienie("krem waniliowy")
ciasto_3.dodaj_dodatki(["proszek kakaowy", "wiórki kokosowe"])

print(oferta_cukierni)
# [<__main__.Ciasto object at 0x1028bcfd0>, <__main__.Ciasto object at 0x1028bcfa0>, <__main__.Ciasto object at 0x1028bcf10>]
print("-" * 30)


print("Dziś w naszej ofercie:")
for ciasto in oferta_cukierni:
    ciasto.pokaz_informacje()

# Dziś w naszej ofercie:
# CIASTO WANILIOWE
# Rodzaj:  ciasto
# Smak:    waniliowe
# Dodatki:
#         czekolada
#         orzechy
# Nadzienie: krem
# --------------------
# MUFFINKA CZEKOLADOWA
# Rodzaj:  muffinka
# Smak:    czekoladowy
# Dodatki:
#         czekolada
# Nadzienie: krem waniliowy
# --------------------
# BEZA SUPER SŁODKA
# Rodzaj:  beza
# Smak:    bardzo słodki
# Dodatki:
#         proszek kakaowy
#         wiórki kokosowe
# --------------------
