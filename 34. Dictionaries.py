movie = {
    "title": "The Life of Scott",
    "year": 1997,
    "cast": ["Kelly", "Joey", "Justice", "Jeremy", "Anna"],
}

print(movie["title"])
# this will give us an error, since budget does not exist.
# print(movies["budget"])

# if we use the dict.get(key) metohd instead of just dict[key], then we will return "None" instead of an Error when the value is not found
print(movie.get("title"))
print(movie.get("budget"))
# we can also pass a default value to output when the key is not found
print(movie.get("budget", "budget not found"))


# we can also reassign values for a key in a dictionary like so:
movie["title"] = "The Life of Ponyo"
print(movie.get("title"))


# we can also create a new key-value pair that doesn't previously exist, like so:
movie["budget"] = 100000
print(movie)


# we can delete values from a dictionary using del dict["key"], but the dict.pop("key") is a better approach
movie.pop("title")
print(movie)


# we can use the dict.keys() function to retrieve all of the keys in a dictionary
print(movie.keys())
# we can use the dict.values() function to retrieve all of the values in the dictionary
print(movie.values())
# and lastly, we can use the dict.items() function to retrieve all of the key:value pairs as a LIST OF TUPLES
print(movie.items())


# we can also create LOOPS to iterate over all of the keys in a dictionary, like so:
for (
    key,
    value,
) in (
    movie.items()
):  # we must do dict.items(); if we just try for key, value in dict: we will get an error
    print(f"{key} : {value}")
