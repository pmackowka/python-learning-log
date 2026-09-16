# Pytanie 26
# - stwórz plik o nazwie "moj_plik.txt"
# - wpisz do niego liczby od 1 do 10, każdą w nowej linijce
# - otwórz plik i zapisz jego zawartosc do listy z_pliku

with (
    open("moj_plik.txt", "w") as f
):  # otwórz plik 'mój_plik.txt' w wersji do zapisu ('w' od write), nadaj mu alias f
    for n in range(1, 11):  # dla kolejnych liczb z zakresu od 1 do 10
        f.write(
            str(n) + "\n"
        )  # wpisz do pliku stringa utworzonego na podstawie liczby oraz znak nowej linii '\n'

with (
    open("moj_plik.txt", "r") as f
):  # otwórz plik 'mój_plik.txt' w wersji do odczytu ('r' od read), nadaj mu alias f
    z_pliku = (
        f.readlines()
    )  # do listy z_pliku wpisz kolejne linijki przeczytane z pliku 'moj_plik.txt'
    # każda linijka będzie osobnym elementem listy
print(z_pliku)
# ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n', '10\n']


with open("moj_plik.txt", "r", encoding="utf-8") as f:
    print(f.read())
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
