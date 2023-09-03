# Mastermind Game README

This is a Python implementation of the classic board game **Mastermind**. In this game, the computer randomly generates a secret code 
consisting of four colors, and the player's goal is to guess the code within a limited number of attempts. The game provides feedback 
on each guess, indicating how many colors are correct and in the correct position and how many colors are correct but in the wrong position.

## Table of Contents

- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Installation](#installation)
- [Usage](#usage)

## How to Play

1. Run the Python script to start the game.
2. You will be presented with a welcome menu with three options:
   - [1] Instruction: Provides information on how to play the game.
   - [2] Start game: Starts the Mastermind game.
   - [3] Exit game: Exits the game.

3. If you choose "Instruction," you will see an explanation of the game rules. To play, return to the welcome menu and select "Start game."

4. In the game, the computer randomly selects a secret code of four colors from a list of six possible colors: RED (R), GREEN (G), BLUE (B), YELLOW (Y), PURPLE (P), and WHITE (W).

5. You must guess the four correct colors in the correct order within a limited number of attempts (8 attempts by default).

6. Enter your guess using the color codes provided in the instructions. For example, if you want to guess "RED GREEN BLUE WHITE," you should enter "RGBW."

7. After each guess, the computer will provide a clue:
   - "0" indicates a correct color in the wrong position.
   - "1" indicates a correct color in the correct position.
   - The clue will help you refine your guesses.

8. Continue guessing until you correctly guess the secret code or run out of attempts.

9. If you guess the correct code, you win the game, and the program will display a congratulatory message along with the number of attempts it took.

10. If you don't guess the correct code within the allowed attempts, the game will reveal the secret code, and you can choose to play again or exit.

## Game Rules

- The secret code consists of four colors in a specific order.
- You have 8 attempts to guess the code correctly.
- You can only use colors from the provided list: RED (R), GREEN (G), BLUE (B), YELLOW (Y), PURPLE (P), and WHITE (W).
- The computer provides clues after each guess to help you refine your next guess.
- To win, you must guess all four colors in the correct order within the allowed attempts.

## Installation

Simply ensure you have Python installed on your system.

## Usage

1. Using an IDE.
   1. Download the Python script (`mastermind_game.py`) to your local machine.
   2. Open an IDE that support Python language and simply run it.
      
2. Using a terminal or command prompt.
   1. Download the Python script (`mastermind_game.py`) to your local machine.   
   2. Open a terminal or command prompt.
   3. Navigate to the directory where the script is located.
   4. Run the script using the following command:
   ```
   python mastermind_game.py
   ```

Have fun playing Mastermind!
