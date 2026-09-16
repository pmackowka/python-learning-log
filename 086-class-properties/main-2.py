"""LAB - Właściwości klasy
W tym LAB pracujemy z klasą z poprzedniej lekcji (jeśli nie masz rozwiązania skopiuj sobie moją propozycję rozwiązania z poprzedniej lekcji)

Do klasy należy dodać atrybut ukryty __text. Odpowiada on za napis umieszczony na torcie.

W funkcji __init__ przyjmij nowy argument text

Zapisz go w zmiennej __text przeprowadzając kontrolę: napis można zapisać w instancji tylko jeżeli kind jest 'cake' lub text jest napisem pustym. Jeśli te warunki nie są spełnione wyświetl diagnostyczny komunikat (print dla Ciebie, żeby było wiadomo co się dzieje)

Dodaj ukrytą funkcję __get_text, która będzie zwracać wartość zapisaną w __text

Dodaj ukrytą funkcje __set_text, która przyjmie dodatkowy argument new_text i zaktualizuje atrybut __text tylko dla wyrobów z kind 'cake'

Zdefiniuj właściwość Text korzystającą z powyższych funkcji.

Tworząc obiekty klasy Cake przekaż dodatkowy argument text - umieść napisy puste lub inne typowo  "tortowe", część poprawnych (czyli napis na torcie) i część niepoprawnych (np. napis na waflu)

Wyświetl wszystkie informacje o wszystkich wypiekach

Spróbuj wstawić do właściwości Text napis na torcie i na innym wypieku nietortowym - prześledź poprawność tych operacji ponownie wyświetlając ofertę cukierni"""


class Cake:
    # Atrybuty klasy
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, text):
        # Inicjalizacja atrybutów instancji
        self.name = name  # Nazwa wypieku
        self.kind = kind  # Rodzaj wypieku (np. tort, ciastko)
        self.taste = taste  # Smak wypieku
        self.additives = additives  # Dodatki do wypieku
        self.filling = filling  # Nadzienie
        self.__text = ""  # Ukryty atrybut na napis

        # Sprawdzanie poprawności dla text
        if kind == "cake" or text == "":
            self.__text = text
        else:
            print(f"Nie można ustawić napisu '{text}' na wypieku '{kind}'.")

        Cake.bakery_offer.append(self)

    def show_info(self):
        # Wyświetlenie informacji o wypieku
        print(f"Nazwa: {self.name}")
        print(f"Rodzaj: {self.kind}")
        print(f"Smak: {self.taste}")
        print(f"Dodatki: {', '.join(self.additives) if self.additives else 'Brak'}")
        print(f"Nadzienie: {self.filling if self.filling else 'Brak'}")
        print(f"Napis na torcie: '{self.__text}'")
        print("-" * 20)

    # Ukryta metoda getter dla atrybutu __text
    def __get_text(self):
        return self.__text

    # Ukryta metoda setter dla atrybutu __text
    def __set_text(self, new_text):
        if self.kind == "cake":
            self.__text = new_text
            print(f"Zmieniono napis na torcie '{self.name}' na '{new_text}'.")
        else:
            print(f"Nie można ustawić napisu '{new_text}' na wypieku '{self.kind}'.")

    # Właściwość dla atrybutu __text
    Text = property(__get_text, __set_text, None, "Właściwość dla napisu na torcie.")


# Tworzenie obiektów klasy Cake
cake_01 = Cake(
    "Tort Czekoladowy",
    "cake",
    "czekoladowy",
    ["orzechy", "posypka"],
    "krem waniliowy",
    "Wszystkiego najlepszego",
)
cake_02 = Cake("Ciastko z Kremem", "cookie", "waniliowe", [], "", "")
cake_03 = Cake(
    "Tort Owocowy",
    "cake",
    "truskawkowy",
    ["truskawki", "bita śmietana"],
    "dżem truskawkowy",
    "Sto lat!",
)
cake_04 = Cake("Wafel z Czekoladą", "waffle", "czekoladowy", [], "", "Smacznego!")

# Wyświetlenie początkowych informacji o wypiekach
print("Początkowa oferta cukierni:")
for cake in Cake.bakery_offer:
    cake.show_info()

# Próba zmiany napisu na torcie i innych wypiekach
cake_01.Text = "Najlepszego!"
cake_02.Text = "Smacznego!"
cake_03.Text = "Dla Ciebie"
cake_04.Text = "Pyszności"

# Wyświetlenie końcowych informacji o wypiekach
print("Końcowa oferta cukierni:")
for cake in Cake.bakery_offer:
    cake.show_info()

# Nie można ustawić napisu 'Smacznego!' na wypieku 'waffle'.
# Początkowa oferta cukierni:
# Nazwa: Tort Czekoladowy
# Rodzaj: cake
# Smak: czekoladowy
# Dodatki: orzechy, posypka
# Nadzienie: krem waniliowy
# Napis na torcie: 'Wszystkiego najlepszego'
# --------------------
# Nazwa: Ciastko z Kremem
# Rodzaj: cookie
# Smak: waniliowe
# Dodatki: Brak
# Nadzienie: Brak
# Napis na torcie: ''
# --------------------
# Nazwa: Tort Owocowy
# Rodzaj: cake
# Smak: truskawkowy
# Dodatki: truskawki, bita śmietana
# Nadzienie: dżem truskawkowy
# Napis na torcie: 'Sto lat!'
# --------------------
# Nazwa: Wafel z Czekoladą
# Rodzaj: waffle
# Smak: czekoladowy
# Dodatki: Brak
# Nadzienie: Brak
# Napis na torcie: ''
# --------------------
# Zmieniono napis na torcie 'Tort Czekoladowy' na 'Najlepszego!'.
# Nie można ustawić napisu 'Smacznego!' na wypieku 'cookie'.
# Zmieniono napis na torcie 'Tort Owocowy' na 'Dla Ciebie'.
# Nie można ustawić napisu 'Pyszności' na wypieku 'waffle'.
# Końcowa oferta cukierni:
# Nazwa: Tort Czekoladowy
# Rodzaj: cake
# Smak: czekoladowy
# Dodatki: orzechy, posypka
# Nadzienie: krem waniliowy
# Napis na torcie: 'Najlepszego!'
# --------------------
# Nazwa: Ciastko z Kremem
# Rodzaj: cookie
# Smak: waniliowe
# Dodatki: Brak
# Nadzienie: Brak
# Napis na torcie: ''
# --------------------
# Nazwa: Tort Owocowy
# Rodzaj: cake
# Smak: truskawkowy
# Dodatki: truskawki, bita śmietana
# Nadzienie: dżem truskawkowy
# Napis na torcie: 'Dla Ciebie'
# --------------------
# Nazwa: Wafel z Czekoladą
# Rodzaj: waffle
# Smak: czekoladowy
# Dodatki: Brak
# Nadzienie: Brak
# Napis na torcie: ''
# --------------------
