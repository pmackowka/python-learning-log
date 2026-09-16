# LAB - Typy zmienne (mutable) i niezmienne (immutable)
# Oto deklaracja zmiennej days:

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# należy utworzyć zmienną workdays, która początkowo będzie zawierać te same elementy co days
# następnie należy usunąć z workdays dni wolne
# na koniec wyświetl days i workdays i upewnij się, że sobota i niedziela zniknęły tylko z listy workdays

workdays = days.copy()
print(days, id(days), workdays, id(workdays))

workdays = workdays[0:-2]
print(days, id(days), workdays, id(workdays))

# ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'] 4313136576 ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'] 4313452288
# ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'] 4313136576 ['mon', 'tue', 'wed', 'thu', 'fri'] 4313187136

print(20 * "-")
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# inicjujac zmienna workdays pamiętaj o copy()
workdays = days.copy()
workdays.remove("sat")
workdays.remove("sun")

print("days: ", days)
print("workdays: ", workdays)
