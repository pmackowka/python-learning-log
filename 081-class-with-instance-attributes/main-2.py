"""LAB - Klasy i atrybuty instancji klasy
Szef cukierni w której pracujesz poprosił Cię o napisanie programu, który koniecznie ma działać obiektowo!

Zaczynamy od zdefiniowania klasy Cake, która ma posiadać atrybuty:

-name opisujące nazwę produktu

-kind opisujący rodzaj wypieku np. torty, ciastka, muffinki, bezy

-taste z głównym smakiem

-additives - zawierający listę dodatków do danego ciasta, np. owoce, posypki, polewy itp, jeżeli ciasto nie ma dodatków, to będzie to pusta lista

-filling - opis nadzienia, jeżeli dane ciasto nie ma nadzienia, to ma to być pusty napis

-... możesz dodać dalsze własne pomysły :)

Po zdefiniowaniu klasy utwórz kilka instancji tej klasy, to dobry moment na wzbogacenie słownictwa w zakresie słodkości w języku angielskim, ale jak wolisz - możesz to robić po polsku

Utwórz listę bakery_offer i dodaj do niej instancje wcześniej utworzonych obiektów klasy Cake

Napisz pętlę przechodzącą przez wszystkie instancje klasy znajdujące się na liście bakery_offer i wyświetl coś w rodzaju (dane pochodzące z instancji zostały wytłuszczone):

Today in our offer:

Vanilla Cake - (cake) main taste: vanilla with additives of ['chocolade', 'nuts'], filled with cream

Chocolade Muffin - (muffin) main taste: chocolade with additives of ['chocolade'], filled with

Super Sweet Maringue - (meringue) main taste: very sweet with additives of [], filled with

UWAGA: w kolejnych lekcjach i kolejnych zadaniach będę kontynuował temat cukierni. W większości przypadków zadanie będzie polegało na rozbudowaniu tej klasy. Jeżeli chcesz wykonać wiecej zadań pozwalających Ci lepiej opanować tematykę klas, podrzucam kilka pomysłów poniżej. Do tych pomysłów nie publikuję propozycji rozwiązań. Za to możesz takie własne rozwiązania i propozycje publikować w sekcji Q&A . Możesz też próbować budowania klas z takimi tematami jak sam zechcesz.

"Sklep z używanymi telefonami komórkowymi"
"Warsztat wulkanizacyjny"
"Inwentaryzacja sprzętu komputerowego w firmie"
"Studio fitness"
"Karty gwarancyjne"
"Firma przewozowa - taxi bagażowe"
"Biuro podróży"

"""


class Ciasto:
    def __init__(self, nazwa, rodzaj, smak, dodatki=None, nadzienie=""):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.smak = smak  # Główny smak
        self.dodatki = dodatki if dodatki else []  # Lista dodatków, domyślnie pusta
        self.nadzienie = nadzienie  # Nadzienie, domyślnie pusty string

    def pokaz_informacje(self):
        # Metoda wyświetlająca szczegóły o wypieku
        print(
            f"{self.nazwa} - ({self.rodzaj}) główny smak: {self.smak} "
            f"z dodatkami: {self.dodatki}, nadziane: {self.nadzienie}"
        )


# Tworzenie instancji klasy Ciasto
ciasto_1 = Ciasto(
    nazwa="Tort Waniliowy",
    rodzaj="tort",
    smak="wanilia",
    dodatki=["czekolada", "orzechy"],
    nadzienie="krem",
)

ciasto_2 = Ciasto(
    nazwa="Muffinka Czekoladowa",
    rodzaj="muffinka",
    smak="czekolada",
    dodatki=["czekolada"],
)

ciasto_3 = Ciasto(nazwa="Super Słodka Beza", rodzaj="beza", smak="bardzo słodki")

oferta_cukierni = [ciasto_1, ciasto_2, ciasto_3]

print("Dziś w naszej ofercie:")
for ciasto in oferta_cukierni:
    ciasto.pokaz_informacje()

# Dziś w naszej ofercie:
# Tort Waniliowy - (tort) główny smak: wanilia z dodatkami: ['czekolada', 'orzechy'], nadziane: krem
# Muffinka Czekoladowa - (muffinka) główny smak: czekolada z dodatkami: ['czekolada'], nadziane:
# Super Słodka Beza - (beza) główny smak: bardzo słodki z dodatkami: [], nadziane:
