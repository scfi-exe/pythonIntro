msg = "Welcome to Python 101: Split and Join"
csv = "Eric,John,Michael,Scott"
friendsList = ["Sheila", "Nora", "Abigail", "Herculia"]

# string.split() separates a string into a list of items - we use (",") to split the items by the commas and createa list
csvList = csv.split(",")
print(csvList)

# now we will do the same thing to the "msg" string, but using space " " as the delimiter to denote where we want to split up the itemsinto a list
msgList = msg.split(" ")
print(msgList)

# we can use DELIMITER.join(string) to turn a STRING into a LIST, example:
print(" ".join(friendsList))
print(" is friends with ".join(friendsList))

# we can also SPLIT a string into a list and then JOIN the list back into a string
# why wouldwe want to do that? well, maybe we want to remove all the whitespace. for example:
print(f"{"".join(msg.split())}")

# a more convenient way to do the above, however, is to use the replace() function to replace " " with "", like so:
print(f"msg.replace(): {(msg.replace(" ", ""))}")
