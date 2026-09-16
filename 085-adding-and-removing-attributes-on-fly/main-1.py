# Ukrywanie właściwości.
# Dodawanie właściwości w locie.


class Samochod:
    liczbaSamochodow = 0  # Atrybuty klasy
    listaSamochodow = []  # Atrybuty klasy

    def __init__(
        self, marka, model, czyPoduszkaOK, czyLakierOK, czyMechanikaOK, czyNaSprzedaz
    ):
        # Metoda inicjalizująca obiekt klasy Samochod
        self.marka = marka  # Atrybuty lub właściwości klasy Samochod
        self.model = model
        self.czyPoduszkaOK = czyPoduszkaOK
        self.czyLakierOK = czyLakierOK
        self.czyMechanikaOK = czyMechanikaOK
        self.__czyNaSprzedaz = czyNaSprzedaz  # Ukryty atrybut
        Samochod.liczbaSamochodow += 1
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


samochod_01 = Samochod(
    "Seat", "Ibiza", True, True, True, False
)  # Instancja klasy Samochod; obiekt Samochod
samochod_02 = Samochod("Opel", "Astra", True, False, True, True)

samochod_02.czyNaSprzedaz = False  # W ten sposób nie nadpiszę ukrytego atrybututu
samochod_02.__czyNaSprzedaz = (
    False  # W ten sposób nie nadpiszę ukrytytego atrybututu, tylko utworzę nowy.
)
samochod_02._Samochod__czyNaSprzedaz = False  # W ten sposób nadpiszę ukryty atrybut !!!

samochod_02.pokazInformacje()
print(vars(samochod_02))
# {'marka': 'Opel', 'model': 'Astra', 'czyPoduszkaOK': True, 'czyLakierOK': False, 'czyMechanikaOK': True, '_Samochod__czyNaSprzedaz': True, '__czyNaSprzedaz': False}

samochod_02.rokProdukcji = 2021  # W ten sposób można dodać dodatkowy atrybut i nie muszę tego robić w metodzie inicjalizującej obiekt klasy Samochod
del samochod_02.rokProdukcji  # W ten sposób usuwam atrybut

samochod_02.TAXI = False
delattr(samochod_02, "TAXI")
print(hasattr(samochod_02, "TAXI"))  # Sprawdzam czy obiekt ma atrybut TAXI
