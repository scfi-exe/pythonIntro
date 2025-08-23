userName = input("What is your name? ")
favColor = input("What is your favorite color? ")

# an f-string is achieved by placing the letter f before the opening quotation, like: f"test"
# we can place variables directly in the quotes of an f-string by using {curlyBrackets}
msg = f"Hello, {userName.title()}! I heard that your favorite color was {favColor.lower()}, is that true?"

print(msg)
