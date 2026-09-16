# Konwersja różnych typów (bool, str, int, list) na wartość logiczną w if.
isOk = True
print("Zmienna", isOk, type(isOk), id(isOk))
if isOk:
    print("TRUE")
# Zmienna True <class 'bool'> 4314612928
# TRUE

print(20 * "-")
isOk = "X"
print("Zmienna", isOk, type(isOk), id(isOk))
if isOk:
    print("TRUE")
# Zmienna X <class 'str'> 4311748272
# TRUE

print(20 * "-")
isOk = 0
print("Zmienna", isOk, type(isOk), id(isOk))
if isOk:
    print("TRUE")
# Zmienna 0 <class 'int'> 4365592848

print(20 * "-")
isOk = []
print("Zmienna", isOk, type(isOk), id(isOk))
if isOk:
    print("TRUE")
# Zmienna [] <class 'list'> 4304633280
