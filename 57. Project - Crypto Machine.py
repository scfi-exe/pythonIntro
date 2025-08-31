print("=== ENIGMA DECODER ===")


def enigmaLight():
    # create keys string
    keys = "abcdefghijklmnopqrstuvwxyz !"
    # generate values string -> just change the original string somehow
    values = keys[::-1]
    print(values)
    # create two dictionaries -> one for encoding, one for decoding
    encryptDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))
    # user input message -> ENCRYPT or DECRYPT?
    msg = input("Input your secret message: ").lower()
    mode = input("Type E to encrypt or D to DECRYPT: ")
    # run encode or decode
    if mode.upper() == "E":
        newMsg = "".join([encryptDict[letter] for letter in msg])
    elif mode.upper() == "D":
        newMsg = "".join([decryptDict[letter] for letter in msg])
    # return result
    return newMsg


print(enigmaLight())

while True:
    restart = input(
        "Input Y to run the program again. Press any other key to exit the program: "
    )
    if restart == "Y":
        print(enigmaLight())
    else:
        print("Have a good day.")
        break
