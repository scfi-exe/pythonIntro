import random

# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names). [x]
# 2. Use a loop to collect their names into a list. [x]
# 3. Ask for exactly 3 prize names (in order) and store them in a list. [x]
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats. (i think this is random.sample(xxx))

participants = []

# for i in range(3):
#     name = input(
#         f"Thanks for entering the raffle! You are participant number {i+1}. What is your name?: "
#     )
#     participants.append(name)

# # separator.join(iterable) --> ", ".join(participants)
# print(f"The current raffle participants are: {", ".join(participants)}")

while True:

    name = input(
        f"Thanks for entering the raffle! What is your name? (type DONE to exit): "
    )
    if name.lower() == "done" and len(participants) < 3:
        print(
            "ERROR: You must have at least three participants in this raffle to begin."
        )
    elif name.lower() == "done":
        break
    else:
        participants.append(name)

print(f"The current raffle participants are: {", ".join(participants)}")
print(f"There are currently {len(participants)} participants in the raffle.")

prizeList = []
for i in range(3):
    prize = input(f"What will prize #{i+1} be?: ")
    prizeList.append(prize)

print(prizeList)

# randomly pick 3 winners
for i in range(3):
    winner = participants[(random.sample(participants))]
    if i == 0:
        print(f"{i+1}. {winner} has won the grand prize: {prizeList[i]}!")
    else:
        print(f"{i+1}. {winner} has won: {prizeList[i]}")
