# Pętla while po indeksie - szukanie sąsiednich elementów spełniających warunek
# (kwadrat kolejnej liczby, ciąg trzech liczb, jednakowa długość sąsiednich słów).
print("------------------------------")

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers) - 1

while i < max:
    print(i, numbers[i], numbers[i + 1])
    if numbers[i] ** 2 == numbers[i + 1]:
        print("\tFOUND!")
    i += 1

# 0 8 18
# 1 18 2
# 2 2 4
#         FOUND!
# 3 4 16
#         FOUND!
# 4 16 5
# 5 5 25
#         FOUND!
# 6 25 4
# 7 4 22
# 8 22 3
# 9 3 3
# 10 3 5
# 11 5 3
# 12 3 9
#         FOUND!
# 13 9 81
#         FOUND!
# 14 81 11
print("------------------------------")

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers) - 2

while i < max:
    print(i, numbers[i], numbers[i + 1], numbers[i + 2])
    if numbers[i] ** 2 == numbers[i + 1] and numbers[i + 1] ** 2 == numbers[i + 2]:
        print("\tFOUND!")

    i += 1

# 0 8 18 2
# 1 18 2 4
# 2 2 4 16
#         FOUND!
# 3 4 16 5
# 4 16 5 25
# 5 5 25 4
# 6 25 4 22
# 7 4 22 3
# 8 22 3 3
# 9 3 3 5
# 10 3 5 3
# 11 5 3 9
# 12 3 9 81
#         FOUND!
# 13 9 81 11
print("------------------------------")

texts = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
i = 0
max = len(texts) - 1

while i < max:
    print(i, texts[i], texts[i + 1])
    if len(texts[i]) == len(texts[i + 1]):
        print("\tFOUND!")

    i += 1

# 0 zero one
# 1 one two
#         FOUND!
# 2 two three
# 3 three four
# 4 four five
#         FOUND!
# 5 five six
# 6 six seven
# 7 seven eight
#         FOUND!
# 8 eight nine
