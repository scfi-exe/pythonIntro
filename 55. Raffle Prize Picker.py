import random

# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names). [x]
# 2. Use a loop to collect their names into a list. [x]
# 3. Ask for exactly 3 prize names (in order) and store them in a list. [x]
# 4. Randomly pick 3 different winners from the participant list. [x]
# 5. Print out who wins which prize and make sure the final one [x]
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats. (i think this is random.sample(xxx))

participants = []

while True:

    name = input(
        f"Thanks for entering the raffle! What is your name? (type DONE to exit this loop): "
    )
    if name.lower() == "done" and len(participants) < 3:
        print(
            "ERROR: You must have at least three participants in this raffle to begin."
        )
    elif name.lower() == "done":
        break
    else:
        participants.append(name)

# print(f"The current raffle participants are: {", ".join(participants)}") #sanity check
# print(f"There are currently {len(participants)} participants in the raffle.") #sanity check

prizeList = []
for i in range(3):
    prize = input(f"What will prize #{i+1} be?: ")
    prizeList.append(prize)

# print(prizeList) #sanity check

# create a new list, winners, by using random.sample() to grab 3 UNIQUE participants
winners = random.sample(participants, 3)

# enumerate over the winners list -> we are able to do "i, winner" because of "enumerate(winner)", otherwise we would get an error
print("=== RAFFLE RESULTS ===")
for i, winner in enumerate(winners):
    if i == 0:
        print(f"{i+1}. {winner} has won the grand prize: {prizeList[i]}!")
    else:
        print(f"{i+1}. {winner} has won: {prizeList[i]}")
