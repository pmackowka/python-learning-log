# Przegląd OOP - klasa, obiekt, atrybuty, metody, argumenty metod, __str__, dziedziczenie, polimorfizm.
print("Klasa")


class Cat:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight


print("\nObiekt klasy")
garfield = Cat(name="Garfield", color="ginger", weight=4.3)
print(garfield)
# <__main__.Cat object at 0x104a37fa0>

print("\nAtrybuty klasy")
greeting = f"Hi {garfield.name}!"
print(greeting)
# Hi Garfield!

print("\nMetody")


class Airplane:
    def __init__(self, model, airline):
        self.model = model
        self.airline = airline

    def describe(self):
        return f"This is a {self.model} operated by {self.airline}."


boeing = Airplane(model="Boeing 737", airline="Delta Airlines")
description = boeing.describe()
print(boeing)
# <__main__.Airplane object at 0x1049eaeb0>
print(description)
# This is a Boeing 737 operated by Delta Airlines.

print("\nArgumenty Metod")


class UserProfile:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def update_email(self, new_email):
        self.email = new_email


user = UserProfile(username="john_doe", email="john@example.com", age=30)
print(user)
# <__main__.UserProfile object at 0x1048bcd60>
user.update_email(new_email="john.new@example.com")

# Print the updated attributes
print(f"Username: {user.username}")
# Username: john_doe
print(f"Email: {user.email}")
# Email: john.new@example.com
print(f"Age: {user.age}")
# Age: 30

print("\nMetoda str")


class Video:
    def __init__(self, title, duration, resolution):
        self.title = title
        self.duration = duration
        self.resolution = resolution

    def __str__(self):
        return f"Video Title: {self.title}, Duration: {self.duration} minutes, Resolution: {self.resolution}"


video_instance = Video("Python Basics", 45, "1080p")
print(video_instance)
# Video Title: Python Basics, Duration: 45 minutes, Resolution: 1080p

print("\nDziedziczenie")


class Publication:
    def __init__(self, title):
        self.title = title

    def print_title(self):
        print(f"Title: {self.title}")


class Article(Publication):
    pass


article = Article("Inheritance in Python")
print(article)
# <__main__.Article object at 0x102d37490>
article.print_title()
# Title: Inheritance in Python

print("\nPrzodkowie i potomkowie")


class Product:
    def __init__(self, name):
        self.name = name

    def describe(self):
        pass


class Electronics(Product):
    def describe(self):
        print("This is an electronic product.")


class Clothing(Product):
    def describe(self):
        print("This is a clothing product.")


phone = Electronics("Smartphone")
shirt = Clothing("T-shirt")

phone.describe()
# This is an electronic product.
shirt.describe()
# This is a clothing product.
