# tuples are essentially the same as lists, but with three major differences
#     1) tuples are IMMUTABLE, meaning that they can't be changed - we can't add/remove values to/from them
#     2) because tuples are a less-complex datatype than lists, they run a lot faster (for indexing, searching, computing)
#     3) a [list] is surrounded by brackets, but a (tuple) is surrounded by parentheses

friends = ["Joey", "Justice", "Ashley", "Phoebe"]

friendsTuple = ("Joey", "Justice", "Ashley", " Phoebe")

print(friends[2:4])
print(friendsTuple[2:4])
