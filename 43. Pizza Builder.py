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
    def __init__(self, size, crustType, toppingsList=None):
        self.size = size
        self.crustType = crustType
        self.toppingsList = toppingsList if toppingsList else []

    def addTopping(self, topping):
        self.toppingsList.append(topping)

    def removeTopping(self, topping):
        if topping in self.toppingsList:
            self.toppingsList.remove(topping)
        else:
            print("Could not find that topping.")

    def nicePrint(self):
        print(f"Pizza Size:\n  - {self.size}\nCrust Type:\n  - {self.crustType}")
        if self.toppingsList:
            print("Toppings: ")
            for topping in self.toppingsList:
                print(f"  - {topping.title()}")
        else:
            print("Toppings: None")


myPizza = Pizza("Large", "Brooklyn Style")
myPizza.addTopping("Pepperoni")
myPizza.addTopping("Cheese")
myPizza.addTopping("Red Sauce")
print("=== MY PIZZA ===")
myPizza.nicePrint()
# print(dir(list))
# print(help)


# secondpizza
friendPizza = Pizza(
    "Medium", "Deep Dish", ["Cheese", "Red Sauce", "Bacon", "Pepperoni"]
)
friendPizza.addTopping("Salami")
print("=== FRIEND PIZZA ===")
friendPizza.nicePrint()
