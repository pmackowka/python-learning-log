# Pętla while - suma z poprzednim elementem, oraz gra "zgadnij liczbę" (z licznikiem prób).
number = 1
previous_number = 0

while number <= 10:
    print(number + previous_number)
    previous_number = number
    number += 1

# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
print("------------------------------")

import random

my_number = random.randint(0, 20)
guess = -1

print("Guess my number!")

while guess != my_number:
    guess = int(input())

    if guess == my_number:
        print("You are right! It was:", my_number)
    elif guess > my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")

print("------------------------------")

import random

my_number = random.randint(0, 20)
guess = -1
trials = 0

print("Guess my number!")

while guess != my_number:
    guess = int(input())
    trials += 1

    if guess == my_number:
        print("You are right! It was:", my_number, "You needed", trials, "trials.")
    elif guess > my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")
