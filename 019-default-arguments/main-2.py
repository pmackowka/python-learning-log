# Kolejny przykład mutowalnego argumentu domyślnego - ten sam efekt uboczny co main-1.py.
def usun_ostatni_element_listy(lista=[1, 1, 1, 1]):
    lista.pop()
    print(lista)


"""Domyślne wartości argumentów funkcji => lista=[1,1,1,1] w Pythonie są obliczane tylko raz w momencie definicji funkcji, a nie za każdym razem, gdy funkcja jest wywoływana."""

usun_ostatni_element_listy()  # [1, 1, 1]
usun_ostatni_element_listy([5, 5, 5])  # [5, 5]
usun_ostatni_element_listy()  # [1, 1]
