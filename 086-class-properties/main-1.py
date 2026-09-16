# Getter i Setter to metody w programowaniu obiektowym używane do:
# - uzyskiwania dostępu do prywatnych atrybutów klasy (getter)
# - oraz zmiany ich wartości (setter).
# Są one stosowane, aby lepiej kontrolować dostęp do atrybutów obiektów i zapewnić enkapsulację.

markaNaPromocji = "Opel"


class Samochod:
    liczbaSamochodow = 0  # Atrybut klasy
    listaSamochodow = []  # Atrybut klasy

    def __init__(
        self, marka, model, czyPoduszkaOK, czyLakierOK, czyMechanikaOK, czyNaSprzedaz
    ):
        # Metoda inicjalizująca obiekt klasy Samochod
        self.marka = marka  # Atrybuty lub właściwości obiektu
        self.model = model
        self.czyPoduszkaOK = czyPoduszkaOK
        self.czyLakierOK = czyLakierOK
        self.czyMechanikaOK = czyMechanikaOK
        self.__czyNaSprzedaz = czyNaSprzedaz  # Ukryty atrybut
        Samochod.liczbaSamochodow += 1  # Jest to atrybut do klasy Samochod, a nie do konkretnej instancji (obiektu). Oznacza to, że wartość tego atrybutu jest wspólna dla wszystkich obiektów klasy.
        Samochod.listaSamochodow.append(self)

    def czyUszkodzony(self):
        # Metoda sprawdzająca, czy samochód jest uszkodzony
        return not (self.czyPoduszkaOK and self.czyMechanikaOK and self.czyLakierOK)

    def pokazInformacje(self):
        # Metoda wyświetlająca informacje o samochodzie
        print(f"{self.marka} {self.model}".upper())
        print(f"Poduszka powietrzna - OK - {self.czyPoduszkaOK}")
        print(f"Lakier - OK - {self.czyLakierOK}")
        print(f"Mechanika - OK - {self.czyMechanikaOK}")
        print(f"NA SPRZEDAŻ - {self.__czyNaSprzedaz}")
        print("-------------------")

    # Getter dla atrybutu __czyNaSprzedaz
    def pobierzCzyNaSprzedaz(self):
        return self.__czyNaSprzedaz

    # Setter dla atrybutu __czyNaSprzedaz
    def ustawCzyNaSprzedaz(self, nowyStatusNaSprzedaz):
        if self.marka == markaNaPromocji:
            self.__czyNaSprzedaz = nowyStatusNaSprzedaz
            print(
                f"Zmieniono status CzyNaSprzedaz na {nowyStatusNaSprzedaz} dla {self.marka}"
            )
        else:
            print(
                f"Nie można zmienić statusu CzyNaSprzedaz. Promocja dotyczy tylko marki {markaNaPromocji}."
            )

    # Właściwość property dla __czyNaSprzedaz
    czyNaSprzedaz = property(
        pobierzCzyNaSprzedaz, ustawCzyNaSprzedaz, None, "Status sprzedaży"
    )


# Tworzenie instancji klasy Samochod
samochod_01 = Samochod("Seat", "Ibiza", True, True, True, False)
samochod_02 = Samochod("Opel", "Astra", True, False, True, True)

# Wyświetlenie początkowego statusu
print("Początkowy status samochodów:")
print("Seat:", samochod_01.czyNaSprzedaz)
print("Opel:", samochod_02.czyNaSprzedaz)

# Zmiana statusu sprzedaży
samochod_01.czyNaSprzedaz = True  # Niepowodzenie, marka nie jest objęta promocją
samochod_02.czyNaSprzedaz = False  # Sukces, zmiana statusu dla marki Opel

# Wyświetlenie końcowego statusu
print("Końcowy status samochodów:")
print("Seat:", samochod_01.czyNaSprzedaz)
print("Opel:", samochod_02.czyNaSprzedaz)

# Początkowy status samochodów:
# Seat: False
# Opel: True
# Nie można zmienić statusu CzyNaSprzedaz. Promocja dotyczy tylko marki Opel.
# Zmieniono status CzyNaSprzedaz na False dla Opel
# Końcowy status samochodów:
# Seat: False
# Opel: False
