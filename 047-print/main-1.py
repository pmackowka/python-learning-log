# Warianty print() - f-string, konkatenacja przez przecinek, parametr sep, znak dzwonka \a.
import os

pwd = os.getcwd()
print(pwd)

name = "Python"
print(f"Cześć, {name}")

name = "Python"
print(f"Cześć, {name}")

name = "John"
age = 25
height = 180.5

print("My name is", name, "and I'm", age, "years old.")
print("My height is", height, "cm.")

print(f"My name is {name} and I'm {age} years old.")
print(f"My height is {height} cm.")

name = "Alice"
age = 30
height = 165.5
print(name, age, height, sep="|")

print("this is bell: \a")

print("TVP1", "TVP2", "TVN", "Polsat", "BBC", "HBO", "MTV", sep=";")

print(
    "I like computers",
    "TVP1",
    "TVP2",
    "TVN",
    "Polsat",
    "BBC",
    "HBO",
    "MTV",
    sep=" but better is ",
)

ProgramName = "BBC"
Item = "News"
Time = "18:00"
print("I like watching", Item, "at", Time, "on", ProgramName, ".")
print("I like watching ", Item, " at ", Time, " on ", ProgramName, ".", sep="")
