# @property, @x.setter, @x.deleter - kontrolowany dostęp do prywatnego atrybutu __isForSale.
promotionBrand = "Opel"


class Car:
    def __init__(self, brand, model, isAirbagOK, isPaintOK, isMechanicsOK, isForSale):
        # Initializer method for the Car class
        self.brand = brand  # Object attributes or properties
        self.model = model
        self.isAirbagOK = isAirbagOK
        self.isPaintOK = isPaintOK
        self.isMechanicsOK = isMechanicsOK
        self.__isForSale = isForSale  # Private attribute

    # Getter for the __isForSale attribute
    def __getIsForSale(self):
        return self.__isForSale

    @property
    def IsForSale(self):
        return self.__isForSale

    @IsForSale.setter
    def IsForSale(self, newIsForSaleStatus):
        if self.brand == promotionBrand:
            self.__isForSale = newIsForSaleStatus
            print(f"Changed IsForSale status to {newIsForSaleStatus} for {self.brand}")
        else:
            print(
                f"Cannot change IsForSale status. Promotion only applies to {promotionBrand} brand."
            )

    @IsForSale.deleter
    def IsForSale(self):
        self.__isForSale = None

    @property
    def CarTitle(self):
        return f"Brand: {self.brand}, Model: {self.model}".title()


car_01 = Car("Seat", "Ibiza", True, True, True, False)

print(car_01.IsForSale)
car_01.IsForSale = True
del car_01.IsForSale
print(car_01.IsForSale)
print(car_01.CarTitle)

# False
# Cannot change IsForSale status. Promotion only applies to Opel brand.
# None
# Brand: Seat, Model: Ibiza
