# Zliczanie nominałów (banknoty/monety) w słowniku, sortowane wypisanie z formatowaniem.
banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = {}

for d in banknotes_coins:
    dict_denominations[d] = 0


dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for k in sorted(dict_denominations.keys()):
    print(f"Denominate: {k:6.2f} - amount {dict_denominations[k]:5}")

# Denominate:   0.01 - amount     0
# Denominate:   0.02 - amount     0
# Denominate:   0.05 - amount     0
# Denominate:   0.10 - amount     0
# Denominate:   0.20 - amount     0
# Denominate:   0.50 - amount     1
# Denominate:   1.00 - amount     0
# Denominate:   2.00 - amount     3
# Denominate:   5.00 - amount     2
# Denominate:  10.00 - amount     0
# Denominate:  20.00 - amount     3
# Denominate:  50.00 - amount     2
# Denominate: 100.00 - amount     2
# Denominate: 200.00 - amount     0
# Denominate: 500.00 - amount     0
