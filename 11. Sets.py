# sets are UNIQUE, so no duplicates can exist
# sets are UNORDERED
# sets are a LOT faster at finding values than lists -- up to 100x faster
# {sets} are surrounded by curly brackets, like [lists] are surrounded by brackets

friendsList = ["Carl", "Joe", "Tom", "Tom"]
friendsSet = {"Carl", "Joe", "Tom", "Tom"}

print(f"Friends List: {friendsList}")
print(f"Friends Set: {friendsSet}")
print(
    'Notice how, despite the List and Set being defined in the same way, the SET is UNORDERED and removes the duplicate value for "Tom".'
)


friends = ["John", "Michael", "Terry", "Eric", "Graham"]
friends_tuple = ("John", "Michael", "Terry", "Eric", "Graham")
friends_set = {"John", "Michael", "Terry", "Eric", "Graham", "Eric"}
my_friends_set = {"Reg", "Loretta", "Colin", "Eric", "Graham"}

# setNameA.intersection(setNameB) will find the interaction of the passed sets
print(f"Intersection: {friends_set.intersection(my_friends_set)}")

# setNameA.union(setNameB) will COMBINE the two passed sets into a single set, with no duplicates
print(f"Union: {friends_set.union(my_friends_set)}")
