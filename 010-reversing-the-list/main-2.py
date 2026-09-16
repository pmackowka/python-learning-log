# Używając dowolnej metody odwróć listę odwroc_mnie i zapisz ją do zmiennej odwrocona.

odwroc_mnie = ["trudne", "takie", "bylo", "nie", "To"]

# 1
odwrocona = list(reversed(odwroc_mnie))
print(odwrocona)

# 2
odwrocona = []
for slowa in odwroc_mnie:
    odwrocona.insert(0, slowa)
print(odwrocona)

# 3
odwrocona = list(odwroc_mnie[::-1])
print(odwrocona)
