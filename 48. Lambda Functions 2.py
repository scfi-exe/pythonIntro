def func(n):
    return n


print(type(func(3)))


def func1(n):
    return lambda a: a * n


doubler = func1(2)
print(doubler(5))
print(type(func1(3)))  # notice how this returns a FUNCTION, not an int!


def priceCalc(start, hourlyRate):
    return lambda hours: start + hourlyRate * hours


walkInCost = priceCalc(10, 30)
print(walkInCost(2))
premiumCost = priceCalc(1, 25)
print(premiumCost(2))

# below, we are creating, printing, and calling the lambda function simultaneously
print((lambda a, b, c: a + b + c)(2, 3, 4))
print((lambda a, b, c=4: a + b + c)(2, 3))  # we can assign default values as well

# we can also give 'args' instead of specific variables, which is lowkey sick because check this out
print((lambda *args: sum(args))(5, 5, 5))
print((lambda *args: sum(args))(8, 8, 8, 8, 8))
