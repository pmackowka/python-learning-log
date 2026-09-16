# *args i **kwargs - zbieranie nadmiarowych argumentów oraz różnica między przekazaniem
# listy/słownika wprost a rozpakowaniem ich przez *, **.
def ByMe(prefix="Please", what="something nice", *args, **kwargs):
    print(prefix, what)  # Please a new car
    print(args)  # ('a', 'b', 'c')
    print(kwargs)  # {'shop': 'market', 'color': 'any'}


ByMe("Please", "a new car", "a", "b", "c", shop="market", color="any")

print("-" * 20)

products = ["milk", "bread", "flakes"]
parameters = {"price": "low", "time": "now"}

ByMe("Please", "a new car", products, parameters)
# Please a new car
# (['milk', 'bread', 'flakes'], {'price': 'low', 'time': 'now'})
# {}

print("-" * 20)

ByMe("Please", "a new car", *products, **parameters)
# Please a new car
# ('milk', 'bread', 'flakes')
# {'price': 'low', 'time': 'now'}
