# Argumenty pozycyjne vs nazwane (keyword) oraz wartość domyślna dla drugiego parametru.
def ByMe(prefix, what):
    print(prefix, what)


ByMe("Please buy me", "a new car")
ByMe(prefix="Please buy me", what="a new car")
ByMe(what="a new car", prefix="Please buy me")


print("-" * 30)


def ByMe(prefix, what="something nice"):
    print(prefix, what)


ByMe("Please")
ByMe(prefix="Please")
