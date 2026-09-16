# Pytanie 21: co wydrukuje się w wyniku wykonania poniższego kodu?

print(1 == True)  # True # == to operator porównania wartości
print(1 == True)  # False # is to operator porównania identyczności/tożsamości

print(id(1), id(1), id(True))  # wydrukuj id integera 1 i booleana True
# 303202608 4303202608 4311155904

print(2**3 == 10 - 2)  # True # wydrukuj wynik porównania wartości dwóch równań

A = [1, 2, 3]  # stworzenie dwóch list o identycznej zawartości
B = [1, 2, 3]  # i przypisanych do innych zmiennych A i B
print(A == B)  # True           # porównanie wartości list A i B
print(A is B)  # False          # porównanie identyczności/tożsamośli list A i B
print(id(A), id(B))
# 4376427904 4376747712

a = "kotek"  # stworzenie dwóch stringów o identycznej zawartości
b = "kotek"  # i przypisanych do innych zmiennych a i b
print(a == b)  # porównanie wartości stringów a i b
print(a is b)  # porównanie identyczności/tożsamości stringów a i b
# True
# True
print(id(a), id(b))
# 4376427952 4376427952
