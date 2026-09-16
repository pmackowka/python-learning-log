# Tożsamość (is) i wartość (==) stringów - id() zmiennej po konkatenacji
# i po slice'owaniu z powrotem do tej samej wartości.
myvar = "Hello Python"
myvar2 = myvar
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print("Czy wartość zmiennej jest taka sama:", myvar == myvar2)
print("Czy zmienna jest taka sama:", myvar is myvar2)
print(id(myvar), id(myvar2))

# Hello Python Hello Python
# <class 'str'> <class 'str'>
# Czy wartość zmiennej jest taka sama: True
# Czy zmienna jest taka sama: True
# 4372856560 4372856560

print(20 * "-")

myvar2 = myvar + "!!"
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print("Czy wartość zmiennej jest taka sama:", myvar == myvar2)
print("Czy zmienna jest taka sama:", myvar is myvar2)
print(id(myvar), id(myvar2))

# Hello Python Hello Python!!
# <class 'str'> <class 'str'>
# Czy wartość zmiennej jest taka sama: False
# Czy zmienna jest taka sama: False
# 4372856560 4373192048

print(20 * "-")

myvar2 = myvar2[:-2]
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print("Czy wartość zmiennej jest taka sama:", myvar == myvar2)
print("Czy zmienna jest taka sama:", myvar is myvar2)
print(id(myvar), id(myvar2))

# Hello Python Hello Python
# <class 'str'> <class 'str'>
# Czy wartość zmiennej jest taka sama: True
# Czy zmienna jest taka sama: False
# 4372856560 4373191984
