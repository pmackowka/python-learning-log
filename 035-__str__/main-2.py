# Różnica między __str__ (print) a __repr__ (repr()) na tej samej klasie.
class Person:
    def __init__(self, name, age):
        self.name = name  # Przechowywanie imienia osoby
        self.age = age  # Przechowywanie wieku osoby

    def __str__(self):
        # Przyjazna dla człowieka reprezentacja obiektu
        return f"{self.name}, {self.age} lat"

    def __repr__(self):
        # Formalna, dokładna reprezentacja obiektu
        return f"Person(name='{self.name}', age={self.age})"


# Tworzenie instancji obiektu
p = Person("Anna", 30)

# Wyświetlenie obiektu z użyciem print() (str)
print(p)  # Wynik: Anna, 30 lat

# Wyświetlenie obiektu z użyciem repr()
print(repr(p))  # Wynik: Person(name='Anna', age=30)
