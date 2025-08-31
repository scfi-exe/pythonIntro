# Dictionary Comprehensions
# Here are Monty Python movies, the years they were produced, and fake people whose favorite movies these are
movies = [
    "And Now for Something Completely Different",
    "Monty Python and the Holy Grail",
    "Monty Python's Life of Brian",
    "Monty Python Live at the Hollywood Bowl",
    "Monty Python's The Meaning of Life",
    "Monty Python Live (Mostly)",
]
year = [1971, 1975, 1979, 1982, 1983, 2014]
names = ["John", "Eric", "Michael", "Graham", "Terry", "TerryG"]


print(list(zip(movies, year)))
# give me a dict ("movies":year) for each movies, year in zip(movies,year)
# if we wanted to do this with a for loop, we can say:
newDict = dict()
for movie, yr in zip(movies, year):
    newDict[movie] = yr

print(newDict)
# now, how can we write a comprehension to do the same thing as above?
newDict1 = {movie: yr for movie, yr in zip(movies, year)}
print("=== TESTING NEW DICT (pause) ===")
print(newDict1)

# what if we ONLY want the movies before 1983? what do we do then?
newDict2 = {
    movie: yr for movie, yr in zip(movies, year) if yr < 1983
}  # this is kinda cracked
print("=== MOVIES BEFORE 1983")
print(newDict2)

# what if we only want movies before 1983 that ALSO start with the word "Monty"?
newDict3 = {
    movie: yr
    for movie, yr in zip(movies, year)
    if yr < 1983 and movie.startswith("Monty")
}
print("=== MOVIES BEFORE 1983 THAT START WITH 'MONTY'")
print(newDict3)


# what if we want a list that prints out movies each person likes?
n1 = [
    [name + "'s favorite movie was " + movie + ", which came out in " + str(yr)]
    for name, movie, yr in zip(names, movies, year)
    if yr < 1981
]
print("=== FAVORITE MOVIES OF THE PEOPLE ===")
print(n1)
