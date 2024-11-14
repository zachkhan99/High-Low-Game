# HighLow.py
# Author: Zach Khan
# Date: March 3, 2023

# A simple "Guess the Number" game that uses a while loop and conditional statements
# to guide the user towards guessing the correct number.

import random

def main():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number, and I'll tell you if you're too high, too low, or correct.")
    print("Good luck!\n")

    play_game()

def play_game():
    number = random.randint(1, 100)
    turns = 0

    while True:
        guess = get_guess(turns + 1)
        turns += 1

        if guess == number:
            print(f"Correct! You guessed the number in {turns} turns.\n")
            break
        elif guess < number:
            print("Too low! Try again.\n")
        else:
            print("Too high! Try again.\n")

    if play_again():
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

def get_guess(attempt):
    while True:
        try:
            guess = int(input(f"Attempt {attempt}: Please enter a number between 1 and 100\n"))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input. Enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def play_again():
    while True:
        response = input("Would you like to play again? (yes/no): ").strip().lower()
        if response in ('yes', 'y'):
            return True
        elif response in ('no', 'n'):
            return False
        else:
            print("Please respond with 'yes' or 'no'.")

if __name__ == "__main__":
    main()
