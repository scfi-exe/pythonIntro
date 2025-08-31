# lambda/anonymous functions allow you to write single-line function definitions that you might use once or a few times and then throw away

print("=== LAMBDA FUNCTIONS ===")


def square(x):
    return x * x


# name = lambda parameter(s): expression

square1 = lambda x: x * x
doubleMult = lambda x, y: x * y
print(square1(3))
print(doubleMult(10, 12))


# let's say we're taking a username and alias from an input box, then we want to clean them up
def nameAndAlias(name, alias):
    return name.strip().title() + " : " + alias.strip().title()


print(nameAndAlias("sCOTT", "gnarlisle"))

nameAndAliasLambda = (
    lambda name, alias: name.strip().title() + " : " + alias.strip().title()
)

print(nameAndAliasLambda("Justice", "Jay"))


# let's try something else,
montyPython = [
    "John Marwood Cleese",
    "Eric Idle",
    "Michael Edward Palin",
    "Terrence Van Gilliam",
    "Terry Graham Perry Jones",
    "Graham Arthur Chapman",
]

# orders the list items alphabetically by their first name and then splits with a space
montyPython.sort(key=lambda name: name.split(" "))
print(montyPython)
# if we wanted to order them by their last name, we can do
montyPython.sort(key=lambda name: name.split(" ")[-1])
print(montyPython)
