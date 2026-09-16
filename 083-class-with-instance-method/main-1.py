# Klasa Car wzbogacona o metody instancji (IsDamaged, getInfo).
class Car:
    def __init__(
        self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK
    ):  # Metoda init
        self.brand = brand  # Atrybuty lub właściwości klasy Car
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isMechanicOK and self.isPaintingOK)

    def getInfo(self):
        print(f"{self.brand} {self.model}".upper())
        print(f"Air Bag - ok - {self.isAirBagOK}")
        print(f"Painting - ok - {self.isPaintingOK}")
        print(f"Mechanic - ok - {self.isMechanicOK}")
        print("-------------------")


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

print("-" * 30)

print(car_01.brand, car_01.model, car_01.IsDamaged())
print(car_02.brand, car_02.model, car_02.IsDamaged())

print("-" * 30)

car_01.getInfo()
car_02.getInfo()

# Seat Ibiza True True True
# Opel Astra True True False
# ------------------------------
# Seat Ibiza False
# Opel Astra True
# ------------------------------
# SEAT IBIZA
# Air Bag - ok - True
# Painting - ok - True
# Mechanic - ok - True
# -------------------
# OPEL ASTRA
# Air Bag - ok - True
# Painting - ok - False
# Mechanic - ok - True
# -------------------
