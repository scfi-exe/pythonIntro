print("=== LAMBDA EXERCISE ===")
# def f(x):
#     return x + 5
# create equivalent lambda function below:
f = lambda x: x + 5
print(f(2))


# def stripSpaces(str):
#     return "".join(str.split(" "))
# create equivalent lambda function below:
stripSpaces1 = lambda str: "".join(str.split(" "))
print(stripSpaces1("   Haaaa   y Is Fo   r Horse s!"))


listA = [1, 2, 3, 4]
listB = [3, 4, 5, 6, 7]
# def joinListNoDuplicates(listA, listB):
#     return list(set(listA, listB))
# create equivalent lambda function below
joinListNoDuplicates1 = lambda listA, listB: list(set(listA + listB))
print(joinListNoDuplicates1(listA, listB))


# imagine you run a fan club, and these are the numbers for member IDs that signed up for an event & you want to sort them
signups = ["MPF104", "MPF20", "MPF2", "MPF17", "MPF3", "MPF45"]
print(
    sorted(signups)
)  # Lexicographic sort --> It will do MF104, MF17, MPF2, MPF20, etc.... it doesn't see it as "MPF104", but rather "MPF1"
# write a lambda function that sorts by the numbers at the backend of these numerically
print(
    sorted(signups, key=lambda id: int(id[3:]))
)  # integer sort, lambda function is used to define the key


# .
# exercise: sort this by score using lambda!
# write code here
# print([playerName for player in list])
print("=== Class Lambda Exercise ===")


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


Eric = Player("Eric", 116700)
John = Player("John", 24327)
Terry = Player("Terry", 150000)
playerList = [Eric, John, Terry]

playerList.sort(reverse=True, key=lambda player: player.score)
print([player.name for player in playerList])
