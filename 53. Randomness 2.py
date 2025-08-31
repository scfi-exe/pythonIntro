import random, string

smallcaps = "abcdefghijklmnopqrstuvwxyz"
largecaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
digits = "0123456789"
# string.ascii_lettrs holds lowercase and uppercase letters a-z
lettersNumbers = string.ascii_letters + string.digits
print(lettersNumbers)


print(
    f"=== 'import string' methods ===\nASCII Lowercase: {string.ascii_lowercase}\nASCII Uppercase:{string.ascii_uppercase}\nDigits: {string.digits}"
)


word = ""
for i in range(7):
    word = word + random.choice(lettersNumbers)

print(word)
