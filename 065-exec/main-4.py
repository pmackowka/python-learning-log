# Jak main-3.py, ale dla funkcji |x^3 - sqrt(x)| (drugi plik procesowany przez main-2.py/main-5.py).
argument_list = []
results_list = []

for i in range(1000000):
    argument_list.append(i / 10)

for x in argument_list:
    results_list.append(abs(x**3 - x**0.5))

print(f"min = {min(results_list)}  max = {max(results_list)}")
