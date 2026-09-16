# eval() formuły matematycznej wpisanej przez użytkownika (x jako argument) dla 100 wartości.
argument_list = []

for i in range(100):
    argument_list.append(i / 10)

formula = input("Please enter a formula, use 'x' as the argument: ")

for x in argument_list:
    print(f"{x:3.1f} {eval(formula):6.2f}")
