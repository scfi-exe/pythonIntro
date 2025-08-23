msg = "Hello, welcome to Python 101: Strings"

print(msg)

# Finds the first instance of the passed string and outputs the count
finder = msg.find("Python")
print("Finder: " + str(finder))


# replaces the first variable with the second variable
replacer = msg.replace("Python", "Java")
print("Replacer: " + str(replacer))

# prints TRUE if "Python" is in the passed string && FALSE otherwise (Expected Result: TRUE)
print("Python" in msg)
# prints FALSE if "Egg" is in the passed string && TRUE otherwise (Expected Result: FALSE)
print("Egg" in msg)
