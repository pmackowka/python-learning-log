# Klasa z atrybutami instancji ustawianymi w __init__ (bez metod) - klasa Car.
class Car:
    def __init__(
        self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK
    ):  # Metoda init
        self.brand = brand  # Atrybuty lub właściwości klasy Car
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK


car_01 = Car("Seat", "Ibiza", True, True, True)  # Instancja klasy Car; obiekt Car
car_02 = Car("Opel", "Astra", True, False, True)

print(
    car_01.brand,
    car_01.model,
    car_01.isAirBagOK,
    car_01.isMechanicOK,
    car_01.isPaintingOK,
)
print(
    car_02.brand,
    car_02.model,
    car_02.isAirBagOK,
    car_02.isMechanicOK,
    car_02.isPaintingOK,
)

# self -  To nazwa wewnętrznej zmiennej instancji, która pozwala odwoływać się do atrybutów i metod tej instancji.
