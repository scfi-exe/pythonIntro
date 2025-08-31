import random, string

# take user input for how many digits they would like their password to be, 1-30
# Bonus: ask whether user wants symbols, numbers, upper/lowercase

lettersNumbers = string.ascii_letters + string.digits


while True:
    try:
        passRange = int(
            input("How many characters would you like your password to be? (5 to 30): ")
        )
        # generate password
        password = ""
        for i in range(passRange):
            password = password + random.choice(lettersNumbers)

        print(f"Your new password is: {password}")

        # raise error if an invalid value is input for passRange
        if passRange < 5 or passRange > 30:
            raise ValueError(passRange)
        break
    except ValueError as err:
        print(f"{err}: Bad Value! Please enter an integer between 5 and 30")
