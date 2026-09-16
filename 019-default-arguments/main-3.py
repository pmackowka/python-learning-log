# Poprawka błędu z main-1/main-2 - domyślny argument None zamiast mutowalnej listy.
def dodaj_do_listy(n, lista=None):  # Domyślnie lista=None
    if lista is None:  # Tworzymy nową listę, jeśli nie przekazano argumentu
        lista = []
    lista.append(n)  # Dodaj n do listy
    print(lista)


dodaj_do_listy(1)  # [1]
dodaj_do_listy(2, [4, 5])  # [4, 5, 2]
dodaj_do_listy(3)  # [3]
