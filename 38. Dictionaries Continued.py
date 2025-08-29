# ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left

# Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

# create stores
freelancers = {
    "name": "freelancing Shop",
    "brian": 70,
    "black knight": 20,
    "biccus diccus": 100,
    "grim reaper": 500,
    "minstrel": -15,
}
antiques = {
    "name": "Antique Shop",
    "french castle": 400,
    "wooden grail": 3,
    "scythe": 150,
    "catapult": 75,
    "german joke": 5,
}
pet_shop = {"name": "Pet Shop", "blue parrot": 10, "white rabbit": 5, "newt": 2}

departmentStore = {}


def updateDeptStore():
    for shop in (freelancers, antiques, pet_shop):
        for k, v in shop.items():
            if k != "name":
                departmentStore.update({k: v})


updateDeptStore()
print(f"=== MORNING DEPARTMENT STORE INVENTORY ===\n{departmentStore}\n")

# create an empty shopping cart and add 1000 coins to user purse
cart = {}
coinPurse = 1000

# loop through stores/dicts
for shop in (freelancers, antiques, pet_shop):
    # inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = (
        input(
            f'=== Welcome to {shop.get("name")}! (type exit to exit store) ===\nWhat do you want to buy?: {shop.items()}\n'
        )
        .lower()
        .strip()
    )

    if buy_item in shop:
        # update the cart
        cart.update({buy_item: shop.get(buy_item)})  # use pop...
        coinPurse = coinPurse - shop.get(buy_item)
        shop.pop(buy_item)
        # set department store back to empty so we can update it with the new values for store stock across all 3 storess
        departmentStore = {}
        updateDeptStore()
    else:
        pass

print(f"=== END-OF-DAY DEPARTMENT STORE INVENTORY ===\n{departmentStore}\n")
print(
    f"You Purchased {", ".join(list(cart.keys()))} Your total cost today was {1000-coinPurse} coins. You change is {coinPurse}. Have a nice day of mayhem!"
)
