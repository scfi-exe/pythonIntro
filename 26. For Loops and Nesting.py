for letter in "Norwegian Blue":
    print(letter)

# prints between the range of 1 and 15, in steps of 3
for steps in range(1, 15, 3):
    print(steps)

# we can also do this with a list
friendsList = ["John", "Harry", "Michael", "George"]
for friend in friendsList:
    print(friend)


# we can also 'for loop' over the LENGTH of a list
for index in range(len(friendsList)):
    print(friendsList[index])

# we can use continue statements to pass multiple values through the loop like so
for friend in friendsList:
    if friend == "Eric":
        print(f"Found {friend}!")
        continue
    elif friend == "Michael":
        print(f"Found {friend}!")
        continue


# nested loops are basically just loops INSIDE of other loops
friends = ["John", "Terry", "Eric"]
for friend in friends:
    for number in [1, 2, 3]:
        print(friend, number)

print("For Loop done!")
