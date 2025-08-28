# honestly this was probably an atrocious way to approach this but whatever it works

print("if elif else - Exercise")
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f


def Calculator():
    operator = input(
        "Input + to add, input - to subtract, input * to multiply, input / to divide, and input TEMP for Celsius to Fahrenheit conversion.: "
    )

    if operator == "+":
        numA = float(input("Please input the first number: "))
        numB = float(input("Please input the second number: "))
        print(f"The results are {numA} + {numB} = {numA + numB}")
    elif operator == "-":
        numA = float(input("Please input the first number: "))
        numB = float(input("Please input the second number: "))
        print(f"The results are {numA} - {numB} = {numA - numB}")
    elif operator == "*":
        numA = float(input("Please input the first number: "))
        numB = float(input("Please input the second number: "))
        print(f"The results are {numA} * {numB} = {numA * numB}")
    elif operator == "/":
        numA = float(input("Please input the first number: "))
        numB = float(input("Please input the second number: "))
        print(f"The results are {numA} / {numB} = {numA/numB}")
    elif operator.lower() == "temp":
        convertCelOrFahr = input(
            "Input F to convert Fahrenheit to Celsius. Input C to convert Celsius to Fahrenheit: "
        )
        if convertCelOrFahr.upper() == "C":
            originTemp = input("Please input the Celsius value you wish to convert: ")
            convertedTemp = float(originTemp) * 9 / 5 + 32
            print(f"The converted Fahrenheit value is equal to: {convertedTemp}")
            return convertedTemp
        elif convertCelOrFahr.upper() == "F":
            originTemp = input(
                "Please input the Fahrenheit value you wish to convert: "
            )
            convertedTemp = (float(originTemp) - 32) * (5 / 9)
            print(f"The converted Celsius value is equal to: {convertedTemp}")
            return convertedTemp

    else:
        print("Invalid input. Please enter one of the following operators: + - * /")
        Calculator()


Calculator()
