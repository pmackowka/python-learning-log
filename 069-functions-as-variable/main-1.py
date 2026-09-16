# Funkcja jako wartość - przypisanie funkcji do zmiennej (bez wywołania) i wywołanie przez nią.
def BuyMe(what):
    print("Give me", what)


BuyMe("a new car")
# Give me a new car

StealForMe = BuyMe
print(StealForMe)
# <function BuyMe at 0x1025281f0>

StealForMe("abc")
# Give me abc


def GoLeft(*args):
    print("PLACEHOLDER - TURNING left with", *args)
