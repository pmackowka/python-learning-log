"""LAB - Dodawanie i ukrywanie atrybutów
W tym zadaniu nadal pracujemy nad klasą "Ciastko"

Dodaj do klasy Cake ukryty atrybut gluten_free. (To jedna z ważniejszych informacji o wypiekach, dlatego staramy się, żeby ten atrybut można było ustawić tylko raz podczas tworzenia obiektu, dzięki czemu później podczas pracy programu nie zmienimy przypadkowo wartości w tym polu)

Zmień funkcję __init__ oraz show_info tak, aby obsługiwały nowy atrybut klasy

Tworząc nowe obiekty wypieków przekazuj wartość True lub False wskazującą na to czy wypiek jest bezglutenowy (o ile wiem jajka nie zawierają glutenu, więc bezy są bezglutenowe)

Przetestuj działanie programu

Spróbuj w kodzie programu (np. po wyświetleniu oferty ciastkarni) zmienić atrybut __gluten_free

Czy po uruchomieniu masz błąd? Dlaczego? Korzystając z polecenia dir(cake03) zobacz jakie atrybuty ma ten obiekt

Zmień wartość atrybutu korzystając ze specjalnie i automatycznie utworzonego atrybutu o specyficznej budowie tak, jak to było zrobione w materiale video

Wyświetl ponownie informacje o cake03 (beza) - czy teraz stała się wyrobem glutenowym?"""


class Ciasto:
    def __init__(self, nazwa, rodzaj, smak, dodatki, nadzienie, bezglutenowe):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.smak = smak
        self.dodatki = dodatki
        self.nadzienie = nadzienie
        self.__bezglutenowe = (
            bezglutenowe  # Ukryty atrybut przechowujący informację o glutenie
        )

    def pokaz_informacje(self):
        print(f"Ciasto: {self.nazwa}")
        print(f"Rodzaj: {self.rodzaj}")
        print(f"Smak: {self.smak}")
        print(f"Dodatki: {', '.join(self.dodatki) if self.dodatki else 'Brak'}")
        print(f"Nadzienie: {self.nadzienie if self.nadzienie else 'Brak'}")
        print(f"Bezglutenowe: {'Tak' if self.__bezglutenowe else 'Nie'}")
        print("-------------------------------")


ciasto01 = Ciasto("Sernik", "sernik", "słodki", ["rodzynki"], None, False)
ciasto02 = Ciasto("Szarlotka", "ciasto owocowe", "jabłkowy", None, None, False)
ciasto03 = Ciasto("Beza", "deser", "słodki", ["bita śmietana"], None, True)

ciasto01.pokaz_informacje()
ciasto02.pokaz_informacje()
ciasto03.pokaz_informacje()

try:
    ciasto03.__bezglutenowe = False
except AttributeError as e:
    print("Błąd:", e)

print("Atrybuty ciasto03:", dir(ciasto03))

ciasto03._Ciasto__bezglutenowe = False
ciasto03.pokaz_informacje()

# Ciasto: Beza
# Rodzaj: deser
# Smak: słodki
# Dodatki: bita śmietana
# Nadzienie: Brak
# Bezglutenowe: Nie
