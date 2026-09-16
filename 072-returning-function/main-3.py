"""Teraz przystąpisz do pisania swojej funkcji generującej inne funkcje:
1. Utwórz funkcję create_function przyjmującą argument span, który może przyjąć wartość:
'm' gdy należy wygenerować funkcję zwracającą różnicę w minutach
'h' gdy należy wygenerować funkcję zwracającą różnicę w minutach
'd' gdy należy wygenerować funkcję zwracającą różnicę w minutach
2. Zainicjuj zmienna sec odpowiednią dla span wartością liczbową, przez którą będziesz dzielił wartość w duration_in_s
3.  Do zmiennej tekstowej source wpisz tekst zawierający definicję dowolnej z początkowych funkcji, np. time_span_m
4. Zmień nazwę funkcji definiowanej w tekście source na f i zamień sztywną wartość liczbową na wartość ze zmiennej sec. Pamiętaj o usunięciu wcięć po lewej stronie - napis musi spełniać warunki formatowania dla Pythonowych funkcji.
5. Poleceniem exec wykonaj kod znajdujący się w zmiennej source. Pamiętaj o przekazaniu środowiska przy pomocy funkcji globals()
6. Zwróć funkcję f

Na tym etapie można sprawdzać efekty swojej pracy
1. Wygeneruj funkcje f_minutes wywołując create_function z parametrem 'm'
2. Wygeneruj funkcje f_hours wywołując create_function z parametrem 'h'
3. Wygeneruj funkcje f_days  wywołując create_function z parametrem 'd'
4. Przetestuj działanie funkcji:"""

from datetime import datetime


def create_function(span):
    if span == "m":
        sec = 60
    elif span == "h":
        sec = 3600
    elif span == "d":
        sec = 86400
    else:
        raise ValueError(
            "Invalid span. Use 'm' for minutes, 'h' for hours, or 'd' for days."
        )

    print(sec)

    source = f"""
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {sec})[0]
    """
    exec(source, globals())
    return f


f_minutes = create_function("m")  # 60
f_hours = create_function("h")  # 3600
f_days = create_function("d")  # 86400

start = datetime(2024, 1, 1, 0, 0, 0)
end = datetime.now()

print("Różnica w minutach:", f_minutes(start, end))
print("Różnica w godzinach:", f_hours(start, end))
print("Różnica w dniach:", f_days(start, end))
