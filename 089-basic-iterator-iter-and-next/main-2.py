# Własny iterator łączący trzy listy (produkty x promocje x klienci) w kombinacje.
import time


# Definicja klasy Combinations
class Combinations:
    def __init__(self, products, promotions, customers):
        # Przechowywanie list produktów, promocji i klientów
        self.products = products
        self.promotions = promotions
        self.customers = customers
        # Indeksy aktualnych elementów
        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Sprawdzenie, czy lista klientów została wyczerpana
        if self.current_customer >= len(self.customers):
            self.current_customer = 0  # Reset indeksu klientów
            self.current_promotion += 1  # Przejście do kolejnej promocji

        # Sprawdzenie, czy lista promocji została wyczerpana
        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0  # Reset indeksu promocji
            self.current_product += 1  # Przejście do kolejnego produktu

        # Sprawdzenie, czy lista produktów została wyczerpana
        if self.current_product >= len(self.products):
            raise StopIteration  # Koniec iteracji

        # Tworzenie aktualnej kombinacji
        item_to_return = f"{self.products[self.current_product]} - {self.promotions[self.current_promotion]} - {self.customers[self.current_customer]}"

        # Przesunięcie indeksu klientów
        self.current_customer += 1

        return item_to_return


# Generowanie danych
products = [f"Product {i}" for i in range(1, 500)]
promotions = [f"Promotion {i}" for i in range(1, 50)]
customers = [f"Customer {i}" for i in range(1, 500)]

# Tworzenie instancji iteratora
combinations = Combinations(products, promotions, customers)

# Iteracja po kombinacjach
for c in combinations:
    pass  # Tu będzie analiza każdej kombinacji

# Zatrzymanie programu na 10 sekund dla sprawdzenia pamięci
time.sleep(10)
