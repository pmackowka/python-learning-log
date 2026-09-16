# range() z krokiem (dodatnim i ujemnym), range jako obiekt leniwy, kopiowanie listy (copy(), slice).
for i in range(10, 20, 2):
    print(i)

print(20 * "-")
for i in range(20, 10, -2):
    print(i)

print(20 * "-")
my_list = range(10)
print(my_list, type(my_list))

print(20 * "-")
my_list = list(range(10))
print(my_list, type(my_list), id(my_list))

print(20 * "-")
my_list2 = my_list.copy()
print(my_list2, type(my_list2), id(my_list2))

print(20 * "-")
my_list3 = my_list2[:]
print(my_list3, type(my_list3), id(my_list3))
