# compile() + exec() - porównanie czasu wykonania z wcześniejszą kompilacją kodu i bez niej.
import time

source = "reportLine += 1"

reportLine = 0

start = time.time()
for x in range(1000):
    exec(source)

stop = time.time()
time_not_compiled = stop - start

"""Funkcja compile konwertuje kod źródłowy (tekstowy) do postaci wewnętrznej (bytecode), co może być używane w exec dla lepszej wydajności lub wielokrotnego użycia.
compile() pozwala wybrać tryb wykonania kodu:
•	'exec' – dla kodu wieloliniowego (funkcje, instrukcje, itp.).
•	'eval' – dla pojedynczego wyrażenia, które zwraca wynik.
•	'single' – do wykonania jednej instrukcji interaktywnie."""


start = time.time()
sourceCompiled = compile(source, "internal variable source", "exec")
for x in range(1000):
    exec(sourceCompiled)

stop = time.time()
time_compiled = stop - start

print(reportLine)  # 2

print("time_not_compiled: ", time_not_compiled)
print("time_compiled: ", time_compiled)
print("Ile razy szybciej: ", time_not_compiled / time_compiled)
