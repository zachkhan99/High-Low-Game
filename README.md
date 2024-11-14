# HighLow Game

**Author:** Zach Khan  
**Date:** March 3, 2023  

This is a simple "Guess the Number" game in Python where the player must guess a randomly chosen number between 1 and 100. The game provides feedback, telling the player whether their guess is too high, too low, or correct. The player can continue guessing until they guess the correct number, and after winning, they have the option to play again.

## Features

- **Random Number Generation**: The game selects a random number between 1 and 100.
- **Hints**: After each guess, the player is told if their guess is too high or too low.
- **Turn Tracking**: The number of attempts is displayed once the player guesses correctly.
- **Replay Option**: After a correct guess, the player is given the option to play again.

## How It Works

1. The program starts by greeting the player and explaining the rules.
2. The player is prompted to guess a number between 1 and 100.
3. The program tells the player if their guess is too high or too low.
4. The player continues guessing until they guess the correct number.
5. Once the correct number is guessed, the game displays the number of attempts taken.
6. The player is asked if they want to play again. If they choose "yes," a new game begins; if they choose "no," the program exits.

## Example Interaction
```bash
Welcome to the Guess the Number Game! I'm thinking of a number between 1 and 100. Try to guess the number, and I'll tell you if you're too high, too low, or correct. Good luck!

Attempt 1: Please enter a number between 1 and 100 50 Too high! Try again.

Attempt 2: Please enter a number between 1 and 100 30 Too low! Try again.

Attempt 3: Please enter a number between 1 and 100 40 Correct! You guessed the number in 3 turns.

Would you like to play again? (yes/no): yes

Attempt 1: Please enter a number between 1 and 100 70 Too high! Try again.
```

## How to Run

1. Clone this repository to your local machine.
2. Open the terminal/command prompt.
3. Navigate to the folder where the file is saved.
4. Run the program with the following command:

   ```bash
   python HighLow.py
   ```

## Future Improvements
- Add difficulty levels (e.g., narrowing the number range or limiting the number of attempts).
- Implement a leaderboard to track best scores (fewest attempts).
- Add hints for when the player is near the correct number (e.g., “Getting warmer!”).
