# eval() vs exec() - modyfikacja zmiennej globalnej i tworzenie nowej zmiennej wewnątrz exec().
var_x = 1
source = "var_x * 2"
print(eval(source))  # 2

print("-" * 30)
var_x = 10
source = "var_x = 5"
print(exec(source))  # None
print(var_x)  # 5


print("-" * 30)
var_x = 10
source = """
new_var = 1
for i in range(var_x):
	print(i * '-')
	new_var += i"""
print(exec(source))
print(var_x)  # 10
print(new_var)  # 46


print("-" * 30)
source = input("Wprowadź wyraenie np. var_x * 666 lub new_var * 666\n\n")
print(eval(source))
