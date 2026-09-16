# Modyfikacja zmiennej globalnej wewnątrz funkcji za pomocą słowa kluczowego global.
g = "jestem globalna"


def f():
    global g
    g = "teraz jestem lokalna"
    print(g)


f()  # teraz jestem lokalna
print(g)  # teraz jestem lokalna
