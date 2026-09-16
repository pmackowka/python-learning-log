"""Korzystając ze "sprytnej" metody pracy z for wyświetl komunikaty w postaci:

The leader of "...nazwa projektu..." is ...imię i nazwisko lidera..."""

projects = ["Brexit", "Nord Stream", "US Mexico Border"]
leaders = ["Theresa May", "Wladimir Putin", "Donald Trump and Bill Clinton"]

for p, l in zip(projects, leaders):
    print("The leader of", p, "is", l)

print("-" * 20)

"""Utwórz kolejną listę z datami rozpoczęcia projektów:"""
dates = ["2016-06-23", "2016-08-29", "1994-01-01"]
"""The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera..."""

for p, d, l in zip(projects, dates, leaders):
    print("The leader of", p, "started", d, "is", l)

print("-" * 20)

"""
Korzystając ze "sprytnego" złożenia enumerate i zip - dodaj do komunikatu dodatkowo numer kolejny projektu rozpoczynając od 1:
...numer kolejny... - The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera..."""

for num, (p, d, l) in enumerate(zip(projects, dates, leaders)):
    print(num + 1, "- The leader of", p, "started", d, "is", l)
