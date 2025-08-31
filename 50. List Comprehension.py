# python comprehensions allow us to create lists, tuples, sets, and even dictionaries with a lot less code
# an evolution of maps and filters together with lambdas, but require less code and easier to understand
# anything you can do with comprehension, you can do with a FOR loop. but the FOR loop route typically requires more coding

# for the first exercise, we will take a list of number and square each number adn then print out the list

# sentence: "give me a list with num squared for each num in numbers"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbersSquared = []
for num in numbers:
    numbersSquared.append(num * 2)

# comprehension verison of the above
numbersSquared1 = [num * num for num in numbers]
print(numbersSquared1)


# let's say we want something else instead
# let's say we want "give me a list with num for each num in numbers if num is even"
evenNumbers = [num for num in numbers if num % 2 == 0]
print(evenNumbers)
# below is the comprehension version of the above code
evenNumbers1 = filter(lambda num: num % 2 == 0, numbers)
print(list(evenNumbers1))


# now, i want a (letter,number) pair for each letter in "spam" and each number in "0123"
letNumPair = []
for letter in "spam":
    for num in range(4):
        letNumPair.append((letter, num))
print(letNumPair)
# comprehension version below
letNumPair1 = [(letter, num) for letter in "spam" for num in range(4)]
print(letNumPair1)
