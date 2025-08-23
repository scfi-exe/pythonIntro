# by setting a variable=value, i.e. age="28", we are setting a DEFAULT value for that variable, in case one doesn't get passed or called in the argument
def greeting(name, age=28):
    print(f"Hello {name}, you are {str(age)}!")


name = input("Enter your name: ")
age = input("Enter your age: ")
greeting(name, age)

# notice how we don't pass a value to the 'age' variable in the greeting() function, so it defaults to our value of 28
greeting("Judith")
