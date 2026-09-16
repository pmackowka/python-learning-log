# Funkcja jako argument innej funkcji - greet(how, name) wywołuje przekazaną funkcję how.
def say_hello(name):
    print(f"Hello {name}!")


def say_good_morning(name):
    print(f"Good morning {name}!")


def greet(how, name):
    how(name)  # say_hello('Captain')


greet(say_hello, "Captain")
# Hello Captain!

print("-" * 30)
