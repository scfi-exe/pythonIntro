python = {
    "John": 35,
    "Eric": 36,
    "Michael": 35,
    "Terry": 38,
    "Graham": 37,
    "TerryG": 34,
}
holy_grail = {
    "Arthur": 40,
    "Galahad": 35,
    "Lancelot": 39,
    "Knight of NI": 40,
    "Zoot": 17,
}
life_of_brian = {"Brian": 33, "Reg": 35, "Stan/Loretta": 32, "Biccus Diccus": 45}


# MEMBERSHIP TEST
print(
    "arthur" in holy_grail
)  # should return True if arthur IS in holy grail --> will return false, since it is not capitalized

people = {}
people1 = {}
people2 = {}

# method 1: UPDATE, allows you to take one dictionary and ADD another dictionary to it
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(sorted(people.items()))


# method 2: COMPREHENSION
for groups in (python, holy_grail):
    people1.update(groups)

print(sorted(people1.items()))


# method 3: UNPACKING (works in Python 3.5 and later)
people2 = {**python, **holy_grail, **life_of_brian}
print(sorted(people2.items()))


print(f"The sum of the ages is: {sum(people.values())}")


# which method should you use?
# well if you just have TWO dictionaries, then METHOD 1 works fine
# if we have MORE than TWO dictionaries to combine, then method 2 (comprehension) and method 3 (unpacking) both work really well since they are one LOC
