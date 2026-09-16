# Pytanie 47 - do czego w Pythonie służą funkcje dir() i help().

print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print("-" * 30)

if __name__ == "__main__":  # blok sprawdzający czy uruchamiamy dany plik bezpośrednio
    pass  # plik uruchomiony bezpośrednio w atrybucie __name__ ma stringa '__main__'
    # plik uruchomiony po zaimportowaniu do innego pliku w atrybucie __name__ ma swoją własną nazwę

print(__file__)
# .../046-dir-help/main-1.py

# dir(obiekt) - wyświetla listę atrybutów danego obiektu
# help(obiekt.metoda) - wyświetla opis danego atrybutu obiektu
# help() - wpisane w linię komend spowoduje otwarcie interaktywnego menu helpa
