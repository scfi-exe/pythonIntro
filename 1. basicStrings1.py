# in this file, we go through some string slicing

testString = "Hello, my name is Scott."

userInput = input("What is your name? ")

# When indexing a string, the left-most value is 0 (i.e., "W")
systemResponse = testString[0:7] + userInput + testString[5:]

print(systemResponse)


userInput2 = input("Do you want to see something cool? (Y/N) ")

if userInput2 == "Y":
    # [::-1] reverses the string
    print(systemResponse[::-1])
elif userInput2 == "N":
    print("Okay, have a good day.")
    exit()
else:
    print("Please input either Y or N as a value.")

exit()
