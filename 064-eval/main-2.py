# eval() z osobnym słownikiem global_vars zamiast pełnego globals() -
# dostęp tylko do wskazanych zmiennych.
var_x = 10
password = "jhjchwcFRWfw434"
source = "var_x + 5"  # Fragment kodu od użytkownika
# source = 'password'  # Fragment kodu od użytkownika

print("-" * 20)

# Stworzenie słownika dla globalnych zmiennych
global_vars = {"var_x": var_x, "password": password}

# Wykonanie kodu z eval
result = eval(source, global_vars)
print(result)  # Oczekiwany wynik: 15
