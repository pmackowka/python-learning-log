# Klasa vs instancja - id(), isinstance(), type(), __class__, vars() dla klasy i dla instancji.
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

print("Id of class is:", id(Car))  # Id of class is: 5316333648
print(
    "Id of instances are:", id(car_01), id(car_02)
)  # Id of instances are: 4307115984 4307115936

print("Czy instancja nalezy do danej klasy:", isinstance(car_01, Car))  # True
print(
    "Czy instancja nalezy do danej klasy za pomocą type:", type(car_01) is Car
)  # <class '__main__.Car'> is Car -> True
print(
    "Czy instancja nalezy do danej klasy za pomocą __class__:", car_01.__class__
)  # <class '__main__.Car'

print("Lista wartości atrybutów instancji:", vars(car_01))
# {'brand': 'Seat', 'model': 'Ibiza', 'isAirBagOK': True, 'isPaintingOK': True, 'isMechanicOK': True}

print("Lista wartości klasy:", vars(Car))
# {'__module__': '__main__', '__init__': <function Car.__init__ at 0x1008248b0>, 'IsDamaged': <function Car.IsDamaged at 0x100824790>, 'getInfo': <function Car.getInfo at 0x100824940>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
