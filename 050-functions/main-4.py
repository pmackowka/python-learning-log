# Jak main-2.py, ale funkcja zwraca wynik (return) zamiast go drukować.
from datetime import date


def DaysToEndOfYear(
    year=date.today().year, month=date.today().month, day=date.today().day
):
    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    return delta.days


print(
    "Date: 2020-12-20 days to end of year: %d" % (DaysToEndOfYear(2020, 12, 20))
)  # Date: 2020-12-20 days to end of year: 11

print(
    "Date: 2020-12-21 days to end of year: %d" % (DaysToEndOfYear(2020, 12, 21))
)  # Date: 2020-12-21 days to end of year: 10

print(
    "Date: TODAY days to end of year: %d" % (DaysToEndOfYear())
)  # Date: TODAY days to end of year: 43
