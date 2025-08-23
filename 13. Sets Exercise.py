# Sets - Exercise

friends = {"John", "Michael", "Terry", "Eric", "Graham"}
my_friends = {"Reg", "Loretta", "Colin", "John", "Graham"}
cars = ["900", "420", "V70", "911", "996", "V90", "911", "911", "S", "328", "900"]

# 1. Check if ‘Eric’ and ‘John’ exist in friends
if "Eric" in friends:
    print("Eric exists in the list")
else:
    print("Eric does not exist in the list.")

if "Eric" and "John" in friends:
    print("Eric and John are on the list.")
else:
    print("Either Eric, John, or both are missing from the list.")

# 2. combine or add the two sets
combinedFriends = friends.union(my_friends)
print(f"Our comined friend group consists of: {combinedFriends}")

# 3. Find names that are in both sets
mutualFriends = friends.intersection(my_friends)
print(f"Our mutual friends are: {mutualFriends}")

# 4. find names that are only in friends
uniqueFriends = friends.difference(my_friends)
print(f"Friends that are unique to the Friends list are: {uniqueFriends}")


# 5. Show only the names who only appear in one of the lists
eitherOrFriends = friends.symmetric_difference(my_friends)
print(
    f"Friends that only appear in one list or the other, but do not overlap, are: {eitherOrFriends}"
)

# 6. Create a new cars-list without duplicates
# turn the list into a set with set(list), to remove all of the duplicate values
# then turn the set back into a list with list(set)
# end result: cars = list(set(cars))
cars = list(set(cars))
print(cars)
