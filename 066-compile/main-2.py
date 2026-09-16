# Przypisujemy ciąg znaków jako kod do zmiennej `source`. Ten kod dodaje 1 do zmiennej `reportLine`.
source = "reportLine += 1"

# Inicjalizujemy zmienną `reportLine` wartością 0, która będzie służyła do zliczania.
reportLine = 0

# Wykonujemy kod zapisany w zmiennej `source` za pomocą funkcji `exec`.
# `exec` dynamicznie interpretuje i wykonuje kod w postaci tekstu.
exec(source)

# Kompilujemy kod zapisany w zmiennej `source` do formy, którą można przekazać do `exec`.
# Używamy funkcji `compile` z trzema argumentami:
# - `source`: kod do kompilacji.
# - `'internal variable source'`: nazwa pliku lub źródła, przydatna w debugowaniu.
# - `'exec'`: tryb wykonania kodu (możliwość wykonania wielu instrukcji).
sourceCompiled = compile(source, "internal variable source", "exec")

# Wykonujemy skompilowany kod. Jest to równoważne wywołaniu `exec` na kodzie w postaci tekstowej.
exec(sourceCompiled)

# Wypisujemy wartość `reportLine`. Powinna wynosić 2, ponieważ kod w `source`
# został wykonany dwukrotnie (raz w `exec`, drugi raz w `exec(sourceCompiled)`).
print(reportLine)
