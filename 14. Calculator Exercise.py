print(
    "Welcome! This calculator will take two number inputs and add, subtract, multiply, or divide them."
)


def start():
    inputInit = int(
        input(
            "Press 1 to add. Press 2 to subtract. Press 3 to multiply. Press 4 to divide. "
        )
    )

    if inputInit == 1:
        x = float(input("Please enter the first number you wish to add: "))
        y = float(input("Please enter the second number you wish to add: "))
        print(f"{x} + {y} = {x+y}")
    elif inputInit == 2:
        x = float(input("Please enter the first number you wish to subtract: "))
        y = float(input("Please enter the second number you wish to subtract: "))
        print(f"{x} - {y} = {x-y}")
    elif inputInit == 3:
        x = float(input("Please enter the first number you wish to multiply: "))
        y = float(input("Please enter the second number you wish to multipy: "))
        print(f"{x} * {y} = {x*y}")
    elif inputInit == 4:
        x = float(input("Please enter the first number you wish to divide: "))
        y = float(input("Please enter the second number you wish to divide by: "))
        floatOrFloor = int(
            input("Press 1 for Float Division. Press 2 for Floor Division.")
        )
        if floatOrFloor == 1:
            decimalPlaces = int(
                input("How many decimal places would you like to round to?")
            )
            floatOutput = round((x / y), decimalPlaces)
            print(f"{x} / {y} = {floatOutput}")
        elif floatOrFloor == 2:
            print(f"{x} / {y} = {x//y}")
        else:
            floatOrFloor

    # determine whether to kill the program OR perform another operation, based on user input
    restartOrKill = input(
        "Press 1 to perform another operation. Press any other key to exit the program. "
    )
    if restartOrKill == "1":
        start()
    else:
        print("Thanks for using this program. Have a good day!")
        quit()


start()
