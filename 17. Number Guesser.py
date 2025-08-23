import random

randomNumber = random.randint(1, 100)

print(randomNumber)


# requests user input once a successful guess is made to determine whether we restart or exit the program
def restartOrKill():
    userInput = input("Press 1 to play again. Press any other key to exit the program.")
    if userInput == "1":
        start()
    else:
        print("Thanks for playing!")


def start():
    programRunning = 1
    print("Hello, and welcome to the random number guesser!")
    userGuess = input("Please guess a number between 1 and 100: ")
    userGuessInt = int(userGuess)

    while programRunning == 1:
        if userGuessInt == randomNumber:
            print("Congratulations, your guess was correct!")
            # ends the loop
            programRunning = 0
            # calls the restart-or-kill sequence
            restartOrKill()
        elif userGuessInt > randomNumber:
            print("Sorry, your guess is incorrect. Try a lower number!")
            userGuess = input("Please guess a number between 1 and 100: ")
            userGuessInt = int(userGuess)
        elif userGuessInt < randomNumber:
            print("Sorry, your guess is incorrect. Try a higher number!")
            userGuess = input("Please guess a number between 1 and 100: ")
            userGuessInt = int(userGuess)


start()
