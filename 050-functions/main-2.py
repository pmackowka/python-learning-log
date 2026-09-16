# Domyślny argument date.today() - druga wersja pokazuje, że jest liczony raz,
# w momencie definicji funkcji, nie przy każdym wywołaniu.
from datetime import date


def DaysToEndOfYear(year, month, day):
    from datetime import date

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)


# DaysToEndOfYear(2024,11,18)
DaysToEndOfYear(day=18, month=11, year=2024)

print("----------------")


def DaysToEndOfYear(
    year=date.today().year, month=date.today().month, day=date.today().day
):

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print("Counting from ", date_today, "days remaining", delta.days)


DaysToEndOfYear(2024, 12, 20)  # Counting from  2024-12-20 days remaining 11
DaysToEndOfYear(
    day=23, month=12, year=2024
)  # Counting from  2024-12-23 days remaining 8
DaysToEndOfYear()  # Counting from  2024-11-18 days remaining 43
DaysToEndOfYear(year=2024)  # Counting from  2024-11-18 days remaining 43
DaysToEndOfYear(year=2024, month=12)  # Counting from  2024-12-18 days remaining 13
DaysToEndOfYear(day=1)  # Counting from  2024-11-01 days remaining 60
