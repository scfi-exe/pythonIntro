import random

# below code is testing the frequency of red and green pulls in 10,000 simulations
bag = ["green"] * 5 + ["red"] * 5
pulls = [random.choice(bag) for _ in range(10000)]
print("Green: ", pulls.count("green"))
print("Red: ", pulls.count("red"))


bag2 = [
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
pulls2 = [random.choice(bag2) for _ in range(10000)]
print("Green: ", pulls2.count("green"))
print("Red: ", pulls2.count("red"))
print("Orange: ", pulls2.count("orange"))
print("Black: ", pulls2.count("black"))
