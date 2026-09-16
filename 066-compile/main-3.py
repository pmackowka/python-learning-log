"""LAB - Funkcja compile()
Nadal pracujemy w zwariowanym ośrodku badawczym. Ponieważ profesorowie mieli problem z umieszczaniem swoich skryptów w odpowiednich katalogach, od tej pory dostarczają tylko wzory, które podlegają przeliczeniom. W tym zadaniu wielokrotnie wyliczysz wartości wyliczane wzorami, a następnie porównasz czasy wykonania w zależności od sposobu interpretacji kodu.

1. Zaimportuj moduł math i time
2. Utwórz listę ze wzorami:"""

import time

formulas_list = ["abs(x**3 - x**0.5)", "abs(math.sin(x) * x**2)"]

argument_list = []
for i in range(1000000):
    argument_list.append(i / 10)

# Pierwsze podejście: Bez optymalizacji (dynamiczne wyliczanie)
print("Wykonanie bez optymalizacji:")
for formula in formulas_list:
    results_list = []
    print(f"Pracuję nad formułą: {formula}")

    start = time.time()

    for x in argument_list:
        results_list.append(eval(formula))

    print(f"Min = {min(results_list)} | Max = {max(results_list)}")
    stop = time.time()
    print(f"Czas wykonania: {stop - start:.2f} sekund\n")

# Drugie podejście: Z optymalizacją (kompilacja kodu)
print("Wykonanie z optymalizacją:")
for formula in formulas_list:
    results_list = []
    print(f"Pracuję nad formułą: {formula}")

    compiled_formula = compile(formula, "<string>", "eval")

    start = time.time()

    for x in argument_list:
        results_list.append(eval(compiled_formula))

    print(f"Min = {min(results_list)} | Max = {max(results_list)}")
    stop = time.time()
    print(f"Czas wykonania: {stop - start:.2f} sekund\n")

# Wykonanie bez optymalizacji:
# Pracuję nad formułą: abs(x**3 - x**0.5)
# Min = 0.0 | Max = 999997000002683.6
# Czas wykonania: 3.24 sekund

# Pracuję nad formułą: abs(math.sin(x) * x**2)
# Min = 0.0 | Max = 9997170253.720783
# Czas wykonania: 3.76 sekund

# Wykonanie z optymalizacją:
# Pracuję nad formułą: abs(x**3 - x**0.5)
# Min = 0.0 | Max = 999997000002683.6
# Czas wykonania: 0.17 sekund

# Pracuję nad formułą: abs(math.sin(x) * x**2)
# Min = 0.0 | Max = 9997170253.720783
# Czas wykonania: 0.18 sekund
