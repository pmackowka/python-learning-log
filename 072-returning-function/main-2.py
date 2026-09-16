"""LAB - Funkcje zwracające funkcje
W tym zadaniu napiszesz funkcję, która będzie w stanie wygenerować 3 funkcje:
f_minutes - obliczającą różnicę między datami i wyrażającą ją w minutach
f_hours - obliczającą różnicę między datami i wyrażającą ją w godzinach
f_days - obliczającą różnicę między datami i wyrażającą ją w dniach
Jeśli już masz pomysł jak to zrobić, to działaj. Poniżej znajdują się bardziej szczegółowe instrukcje.
Oto 3 funkcje, które wykonują wspomniane operacje, ale zostały napisane ręcznie:
"""

from datetime import datetime


def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]


def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]


def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]


start = datetime(2024, 1, 1, 0, 0, 0)
end = datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))
# 483155.0
# 8052.0
# 335.0

"""Jak widać cała różnica jest w liczbie, którą należy podzielić duration_in_s. Są to:
60 dla minut
3600 dla godzin
86400 dla dni
Funkcje można przetestować w ten sposób:"""

from datetime import datetime


def create_time_span_function(divisor):
    def time_span(start, end):
        duration = end - start
        duration_in_s = duration.total_seconds()
        return divmod(duration_in_s, divisor)[0]

    return time_span


f_minutes = create_time_span_function(60)
f_hours = create_time_span_function(3600)
f_days = create_time_span_function(86400)

start = datetime(2024, 1, 1, 0, 0, 0)
end = datetime.now()

print(f"Różnica w minutach: {f_minutes(start, end)}")
print(f"Różnica w godzinach: {f_hours(start, end)}")
print(f"Różnica w dniach: {f_days(start, end)}")
# # Różnica w minutach: 483138.0
# # Różnica w godzinach: 8052.0
# # Różnica w dniach: 335.0
