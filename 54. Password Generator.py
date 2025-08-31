import random, string

# take user input for how many digits they would like their password to be, 1-30
# Bonus: ask whether user wants symbols, numbers, upper/lowercase

lettersNumbers = string.ascii_letters + string.digits


while True:
    passRange = int(
        input("How many characters would you like your password to be? (5 to 30): ")
    )
    if passRange >= 5 and passRange <= 30:
        # generate password
        password = ""
        for i in range(passRange):
            password = password + random.choice(lettersNumbers)

        print(f"Your new password is: {password}")
        break
    elif passRange < 5:
        print(
            "ERROR: Too few characters provided. Please input between 5 and 30 characters."
        )
        pass
    elif passRange > 30:
        print(
            "ERROR: Too many characters provided. Please input between 5 and 30 characters.\n"
        )
    elif type(passRange) == float:
        print("VALUE ERROR: Please input an integer value.")
    else:
        print("VALUE ERROR: Please input an integer value.")
