friends = [
    "Justice",
    "Joey",
    "Phoebe",
    "Hailey",
    "Allison",
    "Adam",
    "Rowan",
    "Paden",
    "Jane",
    "Tev",
    "Neil",
    "Dante",
    "Justin",
    "Rowan",
    "Wayne",
    "Tony",
    "Ashley",
    "Arthur",
    "Matt",
    "Owen",
    "Jimmy",
    "Jordan",
]

# count the # of elements in the list
print(f"Number of items in list: {len(friends)}")

# indexing the list
print(friends[0:2])
print(friends[12:])
print(friends[4:8])

# print the list, friends, in reverse
print(friends[::-1])

# list.index("Owen") tells us what position "Owen" is at in the list
print(f"Owen is position #{friends.index("Owen")} in this list.")
