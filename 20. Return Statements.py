def value_added_tax(amount):
    tax = amount * 0.0875
    totalAmount = tax + amount
    # we can't actually do anything with the outputs of a function unless we RETURN something
    # we can return multiple values using commas
    # we can surround the values in brackets or curly brackets to make a list or a set
    return [tax, totalAmount]


price = value_added_tax(100)

print(f"Value Added Tax: ${price[0]}")
print(f"Total Amount: ${price[1]}")
