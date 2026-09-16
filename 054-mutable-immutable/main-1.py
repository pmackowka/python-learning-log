# int, float, bool, str, tuple, frozenset - obiekty niezmienne (immutable)
# list, set, dict - obiekty zmienne (mutable)

number = 10
print("Nazwa zmiennej", number, id(number))
number += 2
print("Nazwa zmiennej", number, id(number))
# Numer zmiennej 10 4334250576
# Numer zmiennej 12 4334250640

print(20 * "-")
text = "Africa"
print("Nazwa zmiennej", text, id(text))
text += " is hot"
print("Nazwa zmiennej", text, id(text))
# Numer zmiennej Africa 4335639664
# Numer zmiennej Africa is hot 4335640304

print(20 * "-")
list = [1, 2, 3]
print("Nazwa zmiennej", list, id(list))
list.append(4)
print("Nazwa zmiennej", list, id(list))
# Nazwa zmiennej [1, 2, 3] 4343004608
# Nazwa zmiennej [1, 2, 3, 4] 4343004608

print(20 * "-")
list2 = list
print("Nazwa zmiennej2", list2, id(list2))
list2.append(5)
print("Nazwa zmiennej", list, id(list))
print("Nazwa zmiennej2", list2, id(list2))
# Nazwa zmiennej2 [1, 2, 3, 4] 4375543232
# Nazwa zmiennej [1, 2, 3, 4, 5] 4375543232
# Nazwa zmiennej2 [1, 2, 3, 4, 5] 4375543232

print(20 * "-")
list3 = list.copy()
print("Nazwa zmiennej", list, id(list))  # Nazwa zmiennej [1, 2, 3, 4, 5] 4334419392
print("Nazwa zmiennej3", list3, id(list3))  # Nazwa zmiennej3 [1, 2, 3, 4, 5] 4334734912
list3.append(6)
print("Nazwa zmiennej", list, id(list))  # Nazwa zmiennej [1, 2, 3, 4, 5] 4334419392
print(
    "Nazwa zmiennej3", list3, id(list3)
)  # Nazwa zmiennej3 [1, 2, 3, 4, 5, 6] 4334734912
