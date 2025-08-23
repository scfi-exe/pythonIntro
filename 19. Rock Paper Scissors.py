import random


def start():
    print("Welcome to ROCK, PAPER, SCISSORS!")
    print("NOTE: You may type EXIT as an input at any point to exit the game.")
    playerScore = 0
    cpuScore = 0
    gameState = 1

    while gameState == 1:
        cpuRNG = random.randint(1, 3)
        # print(f"[DEBUG] CPU RNG: {cpuRNG}")

        if cpuRNG == 1:
            cpuMove = "Rock"
        elif cpuRNG == 2:
            cpuMove = "Paper"
        elif cpuRNG == 3:
            cpuMove = "Scissors"

        # print(f"[DEBUG] CPU Move: {cpuMove}")

        playerMove = input("Please choose either ROCK, PAPER, or SCISSORS: ").title()

        # print(f"[DEBUG] Player Move: {playerMove}")
        if playerMove == "Exit" and cpuMove == "Rock":
            gameState = 0
            print("Thank you for playing, have a good day!")
        if playerMove == "Exit" and cpuMove == "Paper":
            gameState = 0
            print("Thank you for playing, have a good day!")
        if playerMove == "Exit" and cpuMove == "Scissors":
            gameState = 0
            print("Thank you for playing, have a good day!")
        if playerMove == "Rock" and cpuMove == "Rock":
            print(f"The PLAYER has chosen {playerMove}.")
            print(f"The CPU has chosen {cpuMove}.")
            print("The result is a DRAW. No points have been awarded.")
            print(f"[PLAYER SCORE]: {playerScore} POINTS")
            print(f"[CPU SCORE]: {cpuScore} POINTS")
        if playerMove == "Rock" and cpuMove == "Paper":
            print(f"The PLAYER has chosen {playerMove}.")
            print(f"The CPU has chosen {cpuMove}.")
            print("The CPU wins! One point has been awarded to the CPU.")
            cpuScore = cpuScore + 1
            print(f"[PLAYER SCORE]: {playerScore} POINTS")
            print(f"[CPU SCORE]: {cpuScore} POINTS")
        if playerMove == "Rock" and cpuMove == "Scissors":
            print(f"The PLAYER has chosen {playerMove}.")
            print(f"The CPU has chosen {cpuMove}.")
            print("The PLAYER wins! One point has been awarded to the Player.")
            playerScore = playerScore + 1
            print(f"[PLAYER SCORE]: {playerScore} POINTS")
            print(f"[CPU SCORE]: {cpuScore} POINTS")
        # accounting for playerMove == "Paper" scenarios
        if playerMove == "Paper" and cpuMove == "Rock":
            print(f"The PLAYER has chosen {playerMove}.")
            print(f"The CPU has chosen {cpuMove}.")
            print("The Player wins! One point has been awarded to the Player.")
            playerScore = playerScore + 1
            print(f"[PLAYER SCORE]: {playerScore} POINTS")
            print(f"[CPU SCORE]: {cpuScore} POINTS")
        if playerMove == "Paper" and cpuMove == "Paper":
            print(f"The PLAYER has chosen {playerMove}.")
            print(f"The CPU has chosen {cpuMove}.")
            print("The result is a DRAW. No points have been awarded.")
            print(f"[PLAYER SCORE]: {playerScore} POINTS")
            print(f"[CPU SCORE]: {cpuScore} POINTS")
        if playerMove == "Paper" and cpuMove == "Scissors":
            print(f"The PLAYER has chosen {playerMove}.")
            print(f"The CPU has chosen {cpuMove}.")
            print("The CPU wins! One point has been awarded to the CPU.")
            cpuScore = cpuScore + 1
            print(f"[PLAYER SCORE]: {playerScore} POINTS")
            print(f"[CPU SCORE]: {cpuScore} POINTS")
        # accounting for playerMove == "Scissors" scenarios
        if playerMove == "Scissors" and cpuMove == "Rock":
            print(f"The PLAYER has chosen {playerMove}.")
            print(f"The CPU has chosen {cpuMove}.")
            print("The CPU wins! One point has been awarded to the CPU.")
            cpuScore = cpuScore + 1
            print(f"[PLAYER SCORE]: {playerScore} POINTS")
            print(f"[CPU SCORE]: {cpuScore} POINTS")
        if playerMove == "Scissors" and cpuMove == "Paper":
            print(f"The PLAYER has chosen {playerMove}.")
            print(f"The CPU has chosen {cpuMove}.")
            print("The Player wins! One point has been awarded to the Player.")
            playerScore = playerScore + 1
            print(f"[PLAYER SCORE]: {playerScore} POINTS")
            print(f"[CPU SCORE]: {cpuScore} POINTS")
        if playerMove == "Scissors" and cpuMove == "Scissors":
            print(f"The PLAYER has chosen {playerMove}.")
            print(f"The CPU has chosen {cpuMove}.")
            print("The result is a DRAW. No points have been awarded.")
            print(f"[PLAYER SCORE]: {playerScore} POINTS")
            print(f"[CPU SCORE]: {cpuScore} POINTS")


start()
