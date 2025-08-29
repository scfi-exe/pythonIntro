# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

while True:
    number = input("Please enter in a phone number to format: ")
    # commented out inefficient code
    # number = number.replace("-", "")
    # number = number.replace(",", "")
    # number = number.replace(".", "")
    # number = number.replace(" ", "")
    # number = number.replace("+", "")

    for ch in ["-", " ", "(", ")", "+", "."]:
        number = number.replace(ch, "")

    if len(number) == 10:
        print(f"({number[:3]}) {number[3:6]}-{number[6:]}")
        # commented out inefficient code
        # number = number[:0] + "(" + number[0:]
        # number = number[:4] + ")" + number[4:]
        # number = number[:5] + " " + number[5:]
        # number = number[:9] + "-" + number[9:]
        # print(number)
        break
    else:
        print("ERROR: Please enter exactly 10 digits.")
