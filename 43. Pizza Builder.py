#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores: [x]
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping [x]
# 3. Add a method to remove a topping if it exists [x]
# 4. Add a method to print pizza details:[x]
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary


class Pizza:
    def __init__(self, size, crustType, toppingsList):
        self.size = size
        self.crustType = crustType
        self.toppingsList = toppingsList

    def addTopping(self):
        newTopping = input(
            "What topping would you like to add to your pizza?: "
        ).title()
        self.toppingsList.append(newTopping)
        pass

    def removeTopping(self):
        removedTopping = input("What topping would you like to remove?")
        if removedTopping in self.toppingsList:
            self.toppingsList.remove(removedTopping)
        else:
            print("Could not find that topping.")

    def nicePrint(self):
        print(
            f"Pizza Size: {self.size}\nCrust Type: {self.crustType}\nToppings List: {self.toppingsList}"
        )


pizza1 = Pizza("Small", "Garlic Parmesan", ["Cheese", "Sauce"])

pizza1.addTopping()
pizza1.removeTopping()
pizza1.nicePrint()

# print(dir(list))
# print(help)
