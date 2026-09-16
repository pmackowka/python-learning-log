# Atrybuty klasy (numberOfCars, listOfCars) współdzielone i modyfikowane przez wszystkie instancje.
class Car:
    numberOfCars = 0  # Atrybututy klasy
    listOfCars = []  # Atrybututy klasy

    def __init__(
        self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK
    ):  # Metoda init
        self.brand = brand  # Atrybuty lub właściwości klasy Car
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isMechanicOK and self.isPaintingOK)

    def getInfo(self):
        print(f"{self.brand} {self.model}".upper())
        print(f"Air Bag - ok - {self.isAirBagOK}")
        print(f"Painting - ok - {self.isPaintingOK}")
        print(f"Mechanic - ok - {self.isMechanicOK}")
        print("-------------------")


print(
    "Wartości zmiennych klasy PRZED utworzeniem instancji klasy:",
    Car.numberOfCars,
    Car.listOfCars,
)
# 0 []

car_01 = Car("Seat", "Ibiza", True, True, True)  # Instancja klasy Car; obiekt Car
car_02 = Car("Opel", "Astra", True, False, True)

print(
    "Wartości zmiennych klasy PO utworzeniu instancji klasy:",
    Car.numberOfCars,
    Car.listOfCars,
)
# 2 [<__main__.Car object at 0x100e99fd0>, <__main__.Car object at 0x100e99fa0>]


print("Lista wartości atrybutów instancji:", vars(car_01))
# {'brand': 'Seat', 'model': 'Ibiza', 'isAirBagOK': True, 'isPaintingOK': True, 'isMechanicOK': True}

print("Lista wartości klasy:", vars(Car))
# {'__module__': '__main__', 'numberOfCars': 2, 'listOfCars': [<__main__.Car object at 0x10236dfd0>, <__main__.Car object at 0x10236dfa0>], '__init__': <function Car.__init__ at 0x1023609d0>, 'IsDamaged': <function Car.IsDamaged at 0x102360a60>, 'getInfo': <function Car.getInfo at 0x102360af0>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}


print("Lista wartości atrybutów instancji:", dir(car_01))
# ['IsDamaged', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'brand', 'getInfo', 'isAirBagOK', 'isMechanicOK', 'isPaintingOK', 'listOfCars', 'model', 'numberOfCars']

print("Lista wartości klasy:", dir(Car))
# ['IsDamaged', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'getInfo', 'listOfCars', 'numberOfCars']

print(
    "Value taken from instance:",
    car_01.numberOfCars,
    "Value taken from class",
    Car.numberOfCars,
)
# Value taken from instance: 2 Value taken from class 2

number = Car.numberOfCars = 99
print(number)
# 99
