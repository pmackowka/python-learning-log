# Wartości min/max funkcji |sin(x)*x^2| dla miliona argumentów (dane dla 065-exec/main-2.py).
import math

argument_list = []
results_list = []

for i in range(1000000):
    argument_list.append(i / 10)

for x in argument_list:
    results_list.append(abs(math.sin(x) * x**2))

print(f"min = {min(results_list)}  max = {max(results_list)}")
