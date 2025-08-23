# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color [x]
# 2. extend the function with another  input parameter 'color', that defaults to 'red' [x]
# 3. Capture the color via an input box as variable:color
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
#  adding 1 to the age [x]
# 5. Capitalize first letter of the 'name', and rest are small caps [x]
# 6. Favorite color should be in lowercase [x]


def greeting(name, age=28, favColor="red"):
    # Greets user with 'color' and 'name' from 'input box' and 'age', if available, default age is used
    print("--- GREETINGS, TRAVELER ---")
    print(f"Hello {name}, you will be {str(int(age)+1)} on your next birthday!")
    print(f"We hear you like the color {favColor}!")


name = input("Enter your name: ").title()
age = input("Enter your age: ")
favColor = input("Enter your favorite color: ").lower()
greeting(name, age, favColor)
