import random

friendsList = ["Anna", "Justice", "Ash", "Joey", "Phoebe"]

for i in range(5):
    print(f"This is a float: {random.uniform(0,5)}")
    print(f"This is an integer: {random.randint(5,10)}")
    print(
        f"This is a random range of 1,100, in steps of 5: {random.randrange(0,100,5)}"
    )
    print(f"Selecting a random friend: {random.choice(friendsList)}")
    print(f"Grabbing a random sample of 3 friends: {random.sample(friendsList, 3)}\n")

print(f"Unshuffled Friends List: {friendsList}")
random.shuffle(friendsList)
print(f"Shuffled Friends List: {friendsList}")
