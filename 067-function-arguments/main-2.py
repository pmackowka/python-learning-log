"""LAB - Funkcje i wartości domyślne argumentów
Napisz funkcję show_progress, która będzie wyświetlać linię tekstu powstałą wskutek powtórzenia zadaną ilość razy określonego znaku. Funkcja:

przyjmuje argument character, który określa jaki znak ma być powtarzany

przyjmuje argument how_many, który określa ile razy znak ma być powtórzony

wartość domyślna dla character to gwiazdka

Przetestuj działanie funkcji wywołując ją na różne sposoby np.:"""


def show_progress(how_many, character="*"):
    print(how_many * character)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, "-")
show_progress(15, "+")
