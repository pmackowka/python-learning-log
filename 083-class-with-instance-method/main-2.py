"""LAB - Metody instancji klasy
Do klasy z poprzedniego zadania dodaj 3 metody:

show info, która

wyświetli wielkimi literami nazwę produktu

wyświetli informację o smaku

jeśli produkt ma jakieś dodatki to je wyświetli

jeśli produkt ma nadzienie to je wyświetli

(oczywiście przetestuj działanie funkcji po jej zaimplementowaniu)

set_filling, która

jako argument przyjmie nazwę nadzienia ciasta

zapisze ją w atrybucie filling dla ciasta

(oczywiście przetestuj działanie funkcji)

add_additives, która

jako argument przyjmie listę dodatków

wartości z listy doda do aktualnej listy dodatków

(tę funkcję też przetestuj)

Następnie dodaj do muffinki nadzienie kremowe, a do bezy dodaj kokos i posypkę kakaową. Tak zmodyfikowane wypieki wyświetl. Poniżej zobacz spodziewany efekt:

Today in our offer:
VANILLA CAKE
Kind:    cake
Taste:   vanilla
Additives:
        chocolade
        nuts
Filling: cream
--------------------
CHOCOLADE MUFFIN
Kind:    muffin
Taste:   chocolade
Additives:
        chocolade
Filling: vanilla cream
--------------------
SUPER SWEET MARINGUE
Kind:    meringue
Taste:   very sweet
Additives:
        cocoa powder
        coconuts
--------------------"""


class Ciasto:
    def __init__(self, nazwa, rodzaj, smak, dodatki=None, nadzienie=""):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.smak = smak
        self.dodatki = dodatki if dodatki else []
        self.nadzienie = nadzienie

    def pokaz_informacje(self):
        print(self.nazwa.upper())
        print(f"Rodzaj:    {self.rodzaj}")
        print(f"Smak:      {self.smak}")
        if self.dodatki:
            print("Dodatki:")
            for dodatek in self.dodatki:
                print(f"\t{dodatek}")
        if self.nadzienie:
            print(f"Nadzienie: {self.nadzienie}")
        print("-" * 20)

    def ustaw_nadzienie(self, nadzienie):
        self.nadzienie = nadzienie

    def dodaj_dodatki(self, nowe_dodatki):
        self.dodatki.extend(nowe_dodatki)


ciasto_1 = Ciasto(
    nazwa="Ciasto Waniliowe",
    rodzaj="ciasto",
    smak="waniliowy",
    dodatki=["czekolada", "orzechy"],
    nadzienie="krem",
)

ciasto_2 = Ciasto(
    nazwa="Muffinka Czekoladowa",
    rodzaj="muffinka",
    smak="czekoladowy",
    dodatki=["czekolada"],
)

ciasto_3 = Ciasto(nazwa="Super Słodka Beza", rodzaj="beza", smak="bardzo słodki")

ciasto_2.ustaw_nadzienie("krem waniliowy")
ciasto_3.dodaj_dodatki(["kakao", "wiórki kokosowe"])

oferta_cukierni = [ciasto_1, ciasto_2, ciasto_3]

print("Dzisiejsza oferta:")
for ciasto in oferta_cukierni:
    ciasto.pokaz_informacje()

print("-" * 30)

# Dzisiejsza oferta:
# CIASTO WANILIOWE
# Rodzaj:    ciasto
# Smak:      waniliowy
# Dodatki:
#         czekolada
#         orzechy
# Nadzienie: krem
# --------------------
# MUFFINKA CZEKOLADOWA
# Rodzaj:    muffinka
# Smak:      czekoladowy
# Dodatki:
#         czekolada
# Nadzienie: krem waniliowy
# --------------------
# SUPER SŁODKA BEZA
# Rodzaj:    beza
# Smak:      bardzo słodki
# Dodatki:
#         kakao
#         wiórki kokosowe
# --------------------

# W przeciwieństwie do metody .append(), która dodaje całą sekwencję jako jeden element, .extend() wprowadza każdy element osobno do listy.

lista = [1, 2, 3]
lista.append([4, 5])  # Dodaje listę jako jeden element
print(lista)  # Wynik: [1, 2, 3, [4, 5]]

lista = [1, 2, 3]
lista.extend([4, 5])  # Dodaje każdy element z sekwencji osobno
print(lista)  # Wynik: [1, 2, 3, 4, 5]
