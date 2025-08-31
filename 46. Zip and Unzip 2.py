keys = "this parrot is deceased"
values = "denna papegojan ar avliden"

# splitting the two strings at their whitespaces
keys = keys.split()
values = values.split()
print(keys, values)  # sanity check

englishSwedishDictionary = dict(zip(keys, values))
print(englishSwedishDictionary)


# we can also use dictionary comprehension to create a dictionary
new_dict = {key: value for key, value in zip(keys, values)}
print(new_dict)


# what if we want to take this dictionary apart?
english, swedish = list(englishSwedishDictionary.keys()), list(
    englishSwedishDictionary.values()
)
print(english, swedish)


en1, sv1 = zip(*englishSwedishDictionary.items())
print(en1, sv1)
