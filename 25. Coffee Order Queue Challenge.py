# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price


def orderLoop():
    totalPrice = 0.00
    drinkCount = 0

    while True:
        customerName = input("What is your name? ")
        if customerName.lower() == "done":
            print(f"The total price is ${"{:.2f}".format(totalPrice)}")
            print(f"The number of drinks ordered is {drinkCount}")
            break
        drinkOrder = input("What is your drink order? ")
        if drinkOrder.lower() == "latte":
            totalPrice = totalPrice + 3.50
            drinkCount = drinkCount + 1
        elif drinkOrder.lower() == "americano":
            totalPrice = totalPrice + 3.00
            drinkCount = drinkCount + 1
        elif drinkOrder.lower() == "espresso":
            totalPrice = totalPrice + 2.50
            drinkCount = drinkCount + 1
        else:
            print(f"Warning - {drinkOrder} is not a valid drink on the menu.")


orderLoop()

while True:
    restartOrNot = input("Would you like to start a new order? (Y/N) ")

    if restartOrNot.lower() == "y":
        orderLoop()
    elif restartOrNot.lower() == "n":
        print("Thanks for shopping with us!")
        break
    else:
        print("Invalid input. Please enter Y or N.")
