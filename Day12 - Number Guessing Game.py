# This is an early project designed to assist me in learning Python.
# The Number Guessing Game assigns the user a random number to guess,
# and the user must guess the number within 10 or 5 attempts.
# The program gives hints ("Too high"/"Too low") to assist the user.

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def subtract_attempt(attempts):
    return attempts - 1

def number_guessing_game():
    # Variables
    attempts = 0
    random_number = random.randint(1, 100)

    # Welcome Message
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    # Difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = EASY_LEVEL_TURNS
    else:
        attempts = HARD_LEVEL_TURNS

    game_continue = True
    while game_continue:
        # Allow the user to make their guess
        user_guess = int(input("Make a guess: "))
        print(attempts)

        # Check the user's guess against the random number assigned
        # If the guess is less than the random number, output "Too low." and print "Guess again". If greater than the number, "Too high."
        # If the guess is not == to the random number, subtract an attempt from 'attempts'
        if user_guess == random_number:
            print("Correct! The number was " + str(random_number))
            game_continue = False
        elif user_guess < random_number:
            print("Your guess is too low")
            print("Guess again")
            attempts = subtract_attempt(attempts)
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif user_guess > random_number:
            print("Your guess is too high")
            print("Guess again")
            attempts = subtract_attempt(attempts)
            print(f"You have {attempts} attempts remaining to guess the number.")


        # If the player runs out of lives, cancel the game and print the corresponding message
        if attempts <= 0:
            game_continue = False
            print("You have run out of attempts!")

while input("Would you like to play the Number Guessing Game? (y/n): ") == "y":
    print("\n" * 20)
    number_guessing_game()