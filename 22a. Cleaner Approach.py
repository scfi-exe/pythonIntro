# this is meant to be an attempt at a cleaner solution to the exercise in file #22
operator = input(
    "Please enter an operator (+,-,*,/) or 'F' to convert Fahrenheit to Celsius: "
)
numA = float(input("Please enter the first number: "))

if operator == "F":
    print(f"The converted celsius value is {numA*9/5+32}")
else:
    numB = input("Please enter the second number: ")
    if operator == "+":
        print(f"The result is {numA} + {numB} = {numA + numB}")
    elif operator == "-":
        print(f"The result is {numA} - {numB} = {numA - numB}")
    elif operator == "*":
        print(f"The result is {numA} * {numB} = {numA * numB}")
    elif operator == "/":
        print(f"The result is {numA} / {numB} = {numA / numB}")
    else:
        print("Input error.")
