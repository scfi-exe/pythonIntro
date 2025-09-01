import random

# marbles are replaced into the bag after each round
# print/show output data as you go along
# start the game with 1000 pieces of gold
gold = 1000
# a bag has 10 marbles: 6 green and 4 red
bag = [
    "green",
    "green",
    "green",
    "green",
    "green",
    "black",
    "red",
    "red",
    "red",
    "orange",
]

gameState = True

while gameState:
    bet = int(
        input(f"Current Gold Pieces: {gold}\nHow much gold would you like to bet?: ")
    )  # decide how much gold you will bet
    # draw a marble from a bag (assume it's random)

    if bet > gold:
        print("You cannot bet more gold than you have!")
        continue

    pulledMarble = random.choice(bag)
    print(f"You pulled a {pulledMarble} marble from the bag!")

    # if you draw a green marble --> you win the same amount that you bet
    if pulledMarble == "green":
        gold = gold + bet
        print(f"You won {bet} gold! You now have {gold} gold in your wallet.")
    # if you draw a red marble --> you lose the amount that you bet
    elif pulledMarble == "red":
        gold = gold - bet
        print(f"You lost {bet} gold! You now have {gold} gold in your wallet.")
    # BONUS: Replace two marbles: one BLACK marble that is a 10x winner, and one ORANGE marble that is a 5x loser
    elif pulledMarble == "orange":
        gold = gold - (bet * 5)
        print(f"You lost {bet*5} gold! You now have {gold} gold in your wallet.")
    elif pulledMarble == "black":
        gold = gold + (bet * 10)
        print(f"You won {bet*10} gold! You now have {gold} gold in your wallet.")
    # if you lose HALF of your gold, the game is over (so, if gold drops below 500gp)
    if gold <= 500:
        if gold < 0:
            print("You're in debt! Say goodbye to your daughter's college fund!")
        print(
            f"GAME OVER: You have {gold} gold, which means you dropped below 50% of your original gold."
        )
        break
    # number of rounds/draws should be variable (do you want to play again? yes: pass, no:break)
    else:
        replay = input("Input Y to play again. Input any other key to exit: ")
        if replay.upper() == "Y":
            pass
        else:
            print(f"Thank you for playing! You ended with {gold} gold in your wallet.")
            break
