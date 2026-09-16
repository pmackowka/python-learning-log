# Metody instancji, klasy i statyczne

promotionBrand = "Opel"


class Car:
    carCount = 0  # Class attribute
    carList = []  # Class attribute

    def __init__(self, brand, model, isAirbagOK, isPaintOK, isMechanicsOK, isForSale):
        # Initializer method for the Car class
        self.brand = brand  # Object attributes or properties
        self.model = model
        self.isAirbagOK = isAirbagOK
        self.isPaintOK = isPaintOK
        self.isMechanicsOK = isMechanicsOK
        self.__isForSale = isForSale  # Private attribute
        Car.carCount += 1  # This is an attribute of the Car class, not specific to an instance. It is shared across all objects.
        Car.carList.append(self)

    def isDamaged(self):
        # Method to check if the car is damaged
        return not (self.isAirbagOK and self.isMechanicsOK and self.isPaintOK)

    def showInfo(self):
        # Method to display information about the car
        print(f"{self.brand} {self.model}".upper())
        print(f"Airbag - OK - {self.isAirbagOK}")
        print(f"Paint - OK - {self.isPaintOK}")
        print(f"Mechanics - OK - {self.isMechanicsOK}")
        print(f"FOR SALE - {self.__isForSale}")
        print("-------------------")

    # Getter for the __isForSale attribute
    def getIsForSale(self):
        return self.__isForSale

    # Setter for the __isForSale attribute
    def setIsForSale(self, newIsForSaleStatus):
        if self.brand == promotionBrand:
            self.__isForSale = newIsForSaleStatus
            print(f"Changed IsForSale status to {newIsForSaleStatus} for {self.brand}")
        else:
            print(
                f"Cannot change IsForSale status. Promotion only applies to {promotionBrand} brand."
            )

    # Property for __isForSale
    isForSale = property(getIsForSale, setIsForSale, None, "Sale status")

    @classmethod  # Metoda na poziomie klasy
    def ReadFromText(cls, aText):
        aNewCar = cls(*aText.split(":"))
        return aNewCar

    @staticmethod  # Metoda niezalezna od klasy
    def Convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod  # Metoda niezalezna od klasy
    def Convert_KW_KM(KW):
        return KW * 1.36


lineOfText = "Renault:Megane:True:True:False:False"
car_03 = Car.ReadFromText(lineOfText)
car_03.showInfo()

# RENAULT MEGANE
# Airbag - OK - True
# Paint - OK - True
# Mechanics - OK - False
# FOR SALE - False

print("converting 120 KM to KW", Car.Convert_KM_KW(120))
print("converting 90 KW to KM", Car.Convert_KW_KM(90))
