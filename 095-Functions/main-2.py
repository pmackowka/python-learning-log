# Gra w Hangman - pełna implementacja z funkcjami choose_word() i play_hangman().
import random

# Lista słów do zgadywania
word_list = ["python", "hangman", "programming", "challenge", "developer"]


# Funkcja do wyboru losowego słowa
def choose_word():
    return random.choice(word_list)


# Funkcja gry w Hangman
def play_hangman():
    print("Welcome to Hangman!")

    # Wybór słowa
    word = choose_word()
    word_length = len(word)
    guessed_word = ["_"] * word_length  # Puste miejsca na zgadywane litery
    guessed_letters = set()  # Zbiór zgadywanych liter
    attempts = 6  # Maksymalna liczba prób

    print("Word to guess:", " ".join(guessed_word))

    # Rozgrywka
    while attempts > 0 and "_" in guessed_word:
        print(f"\nAttempts remaining: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        guess = input("Guess a letter: ").lower()

        # Walidacja wejścia użytkownika
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        # Sprawdzanie obecności litery w słowie
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts -= 1

        print("Word to guess:", " ".join(guessed_word))

    # Wynik gry
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)


# Uruchomienie gry
play_hangman()
