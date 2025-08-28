print("Guessing game")
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
# 1. What do I want to repeat?
#  -> The message ie "Please guess a number 1-100. You have {count} guesses left: "
# 2. What do I want to change each time?
#  -> Number of guesses remaining
# 3. How long should we repeat?
#  -> Until the user guesses the correct number OR if # of guesses reaches 0

import random

numberToGuess = random.randint(1, 100)
# print(f"For bugtesting purposes, the number to guess is {numberToGuess}")
startingGuesses = 5
remainingGuesses = startingGuesses


while remainingGuesses >= 1:
    userGuess = int(
        input(
            f"Please guess a number from 1-100. You have {remainingGuesses} guesses left. "
        )
    )

    if userGuess == numberToGuess:
        print("Congratulations! You have guessed the correct number.")
        replayOrQuit = input("Would you like to play again? (Y/N) ")
        if replayOrQuit.lower() == "y":
            numberToGuess = random.randint(1, 100)
            remainingGuesses = startingGuesses
        if replayOrQuit.lower() == "n":
            print("Thanks for playing!")
    else:
        remainingGuesses = remainingGuesses - 1
        if userGuess < numberToGuess:
            print("Nice try, but it's a little higher.")
        elif userGuess > numberToGuess:
            print("Good guess, but it's a little lower")

    if remainingGuesses == 0 and userGuess != numberToGuess:
        print(
            f"Sorry, you have lost the game. The number was {numberToGuess}. Better luck next time!"
        )
        replayOrQuit = input("Would you like to play again? (Y/N) ")
        if replayOrQuit.lower() == "y":
            numberToGuess = random.randint(1, 100)
            remainingGuesses = startingGuesses
        elif replayOrQuit.lower() == "n":
            print("Thanks for playing!")
