"""Poniżej znajduje się definicja klasy z właściwością zdefiniowaną w "standardowy" sposób. Zmień ją tak, żeby właściwości były definiowane przy pomocy dekoratorów"""


class Cake:
    known_kinds = [
        "cake",
        "muffin",
        "meringue",
        "biscuit",
        "eclair",
        "christmas",
        "pretzel",
        "other",
    ]
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        self.kind = kind if kind in self.known_kinds else "other"
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free

        # Właściwość prywatna __text, zarządzana przez dekoratory
        self.__text = text if kind == "cake" else ""
        if kind != "cake" and text:
            print(f">>>>> Text can be set only for cake ({self.name})")

    def show_info(self):
        print(f"{self.name.upper()}")
        print(f"Kind:        {self.kind}")
        print(f"Taste:       {self.taste}")
        if self.additives:
            print("Additives:")
            for a in self.additives:
                print(f"\t\t{a}")
        if self.filling:
            print(f"Filling:     {self.filling}")
        print(f"Gluten free: {self.__gluten_free}")
        if self.__text:
            print(f"Text:        {self.__text}")
        print("-" * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    # Getter właściwości text
    @property
    def text(self):
        return self.__text

    # Setter właściwości text
    @text.setter
    def text(self, new_text):
        if self.kind == "cake":
            self.__text = new_text
        else:
            print(f">>>>> Text can be set only for cake ({self.name})")


# Tworzenie instancji klasy Cake
cake01 = Cake(
    "Vanilla Cake",
    "cake",
    "vanilla",
    ["chocolade", "nuts"],
    "cream",
    False,
    "Happy Birthday Margaret!",
)
cake02 = Cake("Chocolate Muffin", "muffin", "chocolate", ["chocolade"], "", False, "")
cake03 = Cake("Super Sweet Meringue", "meringue", "very sweet", [], "", True, "")
cake04 = Cake("Cocoa Waffle", "waffle", "cocoa", [], "cocoa", False, "Good luck!")

# Wyświetlanie informacji o ofercie
print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

# Ustawianie tekstu dla ciast
cake01.text = "Happy birthday!"
cake02.text = "18"  # Wyświetli ostrzeżenie

# Wyświetlanie informacji po zmianach
for c in Cake.bakery_offer:
    c.show_info()
