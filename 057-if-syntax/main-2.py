# LAB - Skrócona składnia instrukcji if i polecenie pass
# Zapisz poniższe polecenie if w postaci uproszczonej:

price = 123
bonus = 23
bonus_granted = True
if bonus_granted:
    price -= bonus
print(price)

print(20 * "-")
price = 123
bonus = 23
bonus_granted = True
print(price - bonus if bonus_granted else 0)


# Zapisz poniższe polecenie if w postaci uproszczonej:

print(20 * "-")
rating = 4
if rating == 5:
    print("very good")
elif rating == 4:
    print("good")
else:
    print("weak")

print(20 * "-")
print("very good" if rating == 5 else "good" if rating == 4 else "weak")

print(20 * "-")
# Uproszczona wersja z wykorzystaniem słownika
print({5: "very good", 4: "good"}.get(rating, "weak"))
