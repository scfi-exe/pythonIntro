capitals = {"USA": "Washington D.C.", "Russia": "Moscow", "China": "Beijing"}

# shows a list of all properties and methods for the passed object, capitals
print(dir(capitals))
# calls help function in terminal; press "q" on keyboard to exit
print(help(capitals))


print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("That capital does not exist.")

keys = capitals.keys()

# get all keys in dictionary
for key in capitals.keys():
    print(key)

# get all values in dictionariy
values = capitals.values()
print(values)

# get all values in dictionariy
for values in capitals.values():
    print(values)

# printing all items (i.e., printing every key:value pair as a tuple)
print(capitals.items())
for item in capitals.items():
    print(item)

# this is cracked
for key, value in capitals.items():
    print(f"{key} : {value}")
