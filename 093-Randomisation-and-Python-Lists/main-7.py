# Gra kamień-papier-nożyce - input(), walidacja wyboru, quit() przy błędnym wejściu, ASCII-art.
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

try:
    user = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
    )
    if user not in [0, 1, 2]:
        print("Invalid choice! Please choose 0 (Rock), 1 (Paper), or 2 (Scissors).")
        quit()
except ValueError:
    print("Invalid input! Please enter a number: 0 (Rock), 1 (Paper), or 2 (Scissors).")
    quit()

computer = random.randint(0, 2)

print(f"\nYou chose:\n{choices[user]}")
print("The computer chose:")
print(choices[computer])

if (user + 1) % 3 == computer:
    print("You lost!")
elif user == computer:
    print("It's a tie!")
else:
    print("You win!")

print("\nThank you for playing!")
