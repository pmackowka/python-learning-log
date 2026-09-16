"""LAB - Funkcja eval()
W tym zadaniu stworzysz mały kalkulator. Użytkownik wprowadzi wzór funkcji np.:

2*x
math.sin(x)
3*x**2+2*x-4

a program wyznaczy wartości tej funkcji dla x z przedziału (0,10) z dokładnością 0.1
1. Zaimportuj moduł math
2. Utwórz pustą listę argument_list
3. Napisz pętlę, która do listy argument_list doda 100 wartości zaczynając od zera gdzie każda kolejna jest o 0.1 większa od poprzedniej
4. Poproś użytkownika o wprowadzenie wzoru. Wzór zapisz w zmiennej formula. Użytkownik wprowadzając ten wzór powinien skorzystać ze zmiennej x do tego aby oznaczyć argument funkcji
5. Dla każdego elementu x z listy argument_list oblicz wartość funkcji wprowadzonej przez użytkownika i wyświetl jej wynik"""

argument_list = []

x = 0
while x <= 10:
    argument_list.append(x)
    x += 0.1

formula = input("Podaj jedną z formuł np.: 2*x lub math.sin(x) lub 3*x**2+2*x-4\n\n")

for x in argument_list:
    print(f"Argument: {x:.1f}, Wynik formuły  {eval(formula):.2f}")
