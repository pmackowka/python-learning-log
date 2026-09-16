# Skopiuj zawartość listy L do zmiennej K
# W liście L pod indeksem 1 umieść stringa 'jeden'
# W liście K pod indeksem 1 umieść stringa 'JEDEN'
# Wydrukuj obie listy w osobnych linijkach

L = [0, 1, 2, 3]
K = L[:]

L[1] = "jeden"
K[1] = "JEDEN"

print(L)
print(K)
# [0, 'jeden', 2, 3]
# [0, 'JEDEN', 2, 3]
