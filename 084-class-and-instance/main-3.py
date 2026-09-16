"""LAB - Klasa a instancja
Pracujemy z wynikiem LAB z poprzedniej lekcji.

Dodaj do klasy Cake atrybut na poziomie klasy. Nazwij go known_kinds. Będą w nim przechowywane produkowane w naszej cukierni słodkości. Przypisz do zmiennej listę np. w następującej postaci:

['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']

Zmień __init__ tak, że jeżeli jako parametr kind zostanie przekazana wartość znajdująca się na liście known_kinds, to zostanie zaakceptowana, ale jeśli ktoś przekaże wartość spoza tej listy, to do nowo tworzonego obiektu do atrybutu kind zostanie wpisany napis other.

Przetestuj działanie nowej funkcji __init__ tworząc obiekt "wafel kakaowy":

cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')



Dodaj do klasy Cake nowy atrybut bakery_offer, który na początku będzie pustą listą.

Zmień __init__ tak, aby po utworzeniu nowego obiektu typu Cake, został on automatycznie dodany do listy bakery_offer

Usuń ze skryptu niepotrzebne już instrukcje tworzące listę bakery_offer i dodające obiekty tej klasy do tej listy.

Zmień pętlę wyświetlającą informację o ofercie cukierni tak, aby korzystała z atrybutu klasy



Sprawdź czy obiekty cake01 i inne są instancjami klasy Cake korzystając z funkcji isinstance i type

Wyświetl informacje o instancji cake01 i o klasie Cake korzystając z funkcji vars i dir"""


class Ciasto:
    znane_rodzaje = [
        "ciasto",
        "muffin",
        "beza",
        "herbatnik",
        "ekler",
        "świąteczne",
        "precel",
        "inne",
    ]
    oferta_cukierni = []

    def __init__(self, nazwa, rodzaj, smak, dodatki, nadzienie):
        self.nazwa = nazwa
        self.rodzaj = rodzaj if rodzaj in Ciasto.znane_rodzaje else "inne"
        self.smak = smak
        self.dodatki = dodatki.copy()
        self.nadzienie = nadzienie
        Ciasto.oferta_cukierni.append(self)

    def pokaz_informacje(self):
        print(f"{self.nazwa.upper()}")
        print(f"Rodzaj:    {self.rodzaj}")
        print(f"Smak:     {self.smak}")
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


ciasto01 = Ciasto(
    "Ciasto Waniliowe", "ciasto", "waniliowe", ["czekolada", "orzechy"], "krem"
)
ciasto02 = Ciasto("Czekoladowy Muffin", "muffin", "czekoladowy", ["czekolada"], "")
ciasto03 = Ciasto("Super Słodka Beza", "beza", "bardzo słodka", [], "")
ciasto04 = Ciasto("Wafel Kakaowy", "wafel", "kakaowy", [], "kakao")

ciasto02.ustaw_nadzienie("waniliowy krem")
ciasto03.dodaj_dodatki(["proszek kakaowy", "wiórki kokosowe"])

print("Dziś w naszej ofercie:")
for ciasto in Ciasto.oferta_cukierni:
    ciasto.pokaz_informacje()

# Sprawdzanie, czy obiekty są instancjami klasy Ciasto
print(isinstance(ciasto01, Ciasto))  # True
print(isinstance(ciasto04, Ciasto))  # True
print(type(ciasto01))  # <class '__main__.Ciasto'>
print(type(ciasto04))  # <class '__main__.Ciasto'>

# Wyświetlenie atrybutów instancji i klasy
print(vars(ciasto01))  # Atrybuty instancji ciasto01
print(vars(Ciasto))  # Atrybuty klasy Ciasto
print(dir(ciasto01))  # Wszystkie dostępne metody i atrybuty instancji ciasto01
print(dir(Ciasto))  # Wszystkie dostępne metody i atrybuty klasy Ciasto

# Dziś w naszej ofercie:
# CIASTO WANILIOWE
# Rodzaj:    ciasto
# Smak:     waniliowe
# Dodatki:
#         czekolada
#         orzechy
# Nadzienie: krem
# --------------------
# CZEKOLADOWY MUFFIN
# Rodzaj:    muffin
# Smak:     czekoladowy
# Dodatki:
#         czekolada
# Nadzienie: waniliowy krem
# --------------------
# SUPER SŁODKA BEZA
# Rodzaj:    beza
# Smak:     bardzo słodka
# Dodatki:
#         proszek kakaowy
#         wiórki kokosowe
# --------------------
# WAFEL KAKAOWY
# Rodzaj:    inne
# Smak:     kakaowy
# Nadzienie: kakao
# --------------------
# True
# True
# <class '__main__.Ciasto'>
# <class '__main__.Ciasto'>
# {'nazwa': 'Ciasto Waniliowe', 'rodzaj': 'ciasto', 'smak': 'waniliowe', 'dodatki': ['czekolada', 'orzechy'], 'nadzienie': 'krem'}
# {'__module__': '__main__', 'znane_rodzaje': ['ciasto', 'muffin', 'beza', 'herbatnik', 'ekler', 'świąteczne', 'precel', 'inne'], 'oferta_cukierni': [<__main__.Ciasto object at 0x10445fb20>, <__main__.Ciasto object at 0x10445faf0>, <__main__.Ciasto object at 0x10445fa60>, <__main__.Ciasto object at 0x10445f940>], '__init__': <function Ciasto.__init__ at 0x10444c8b0>, 'pokaz_informacje': <function Ciasto.pokaz_informacje at 0x10444c790>, 'ustaw_nadzienie': <function Ciasto.ustaw_nadzienie at 0x10444c940>, 'dodaj_dodatki': <function Ciasto.dodaj_dodatki at 0x10444c9d0>, '__dict__': <attribute '__dict__' of 'Ciasto' objects>, '__weakref__': <attribute '__weakref__' of 'Ciasto' objects>, '__doc__': None}
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'dodaj_dodatki', 'dodatki', 'nadzienie', 'nazwa', 'oferta_cukierni', 'pokaz_informacje', 'rodzaj', 'smak', 'ustaw_nadzienie', 'znane_rodzaje']
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'dodaj_dodatki', 'oferta_cukierni', 'pokaz_informacje', 'ustaw_nadzienie', 'znane_rodzaje']
