friends = ["Justice", "Joey", "Phoebe", "Tevye", "Adam"]
ages = [27, 27, 25, 30, 25]
cars = ["Civic", "Corolla", "911", "Camry", "Rogue"]

# prints friends in the order we appended the values to the list
print(friends)

# sorts friends alphabetically
friends.sort()
print(f"Sorted friends: {friends}")

# sorts friends in alphabetical-reverse (NOTE: this is different from REVERSING the list itself)
friends.sort(reverse=True)
print(f"Friends, sorted in alphabetical reverse: {friends}")

# see the difference?
print("Friends sorted in reverse: {friends[::-1]}")


# we can also see the min, max, and the sum of a list
print(f"Minimum Age: {min(ages)}")
print(f"Maximum Age: {max(ages)}")
print(f"Sum of Ages: {sum(ages)}")


# if we want, we can add to a list via append(), like so:
print(f"Before appending this list, I have {friends}")
# appending the list to add "Paden"
friends.append("Paden")
print(f"Now that I have appended this list, I have {friends}")

# we can also use the "Insert" function to specify exactly where we want them in the list
friends.insert(3, "Carl")
print(f"I have now inserted Carl into position 3 (counting up from 0). See: {friends}")

# I can also replace an element in a list, like so:
friends[3] = "Shawn"
print(f"Now, I have replaced Carl's value in the list with Shawn. See: {friends}")

# I can also put two lists together by EXTENDING the list
friends.extend(ages)
print(f"I have extended the list to include their cars: {friends}")

# I can also remove elements, like so:
friends.remove(27)
friends.remove(25)
print(f"I have removed the duplicate instances of 27 and 25 from this list {friends}")

# we can also use the command POP() to remove, which does something slightly different


# we can also remove the WHOLE list by clearing the list
friends.clear()
print(f"Now, we have no friends. See: {friends}")


# we can use "del friends" to delete a list completely from meomry
del friends

# we can use "del" to also delete parts of a list, i.e., "del friends[2:5]"


# ways to copy a list
# 1
newCars = cars[:]
# 2
newCars = cars.copy()
# 3
newCars = list(cars)
