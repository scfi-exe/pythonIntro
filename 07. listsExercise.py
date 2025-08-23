# the lists show profit of lemonade sold each week
# profit for each lemonade sold is $1.50
# add another sale to the sales_w2 list **by capturing a number as an input**
# combine the two lists into the list called "sales"
# calculate/print how much you have earned on:
#   1. your best day (separately)
#   2. your worst day (separately)
#   3. your best and worst day combined


sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []

# add another sale to the sales_w2 list **by capturing a number as an input**
salesInput = int(
    input("How many glasses of lemonade did you sell on the final day of week two? ")
)

sales_w2.append(salesInput)

# combine the two lists into the list called "sales"
# sales.extend(sales_w1)
# sales.extend(sales_w2)
sales = sales_w1 + sales_w2

# calculate/print how much you have earned on:
#   1. your best day (separately)
print(f"On our best day, we earned ${(max(sales)*1.50)}.")
#   2. your worst day (separately)
print(f"On our worst day, we earned ${min(sales)*1.50}.")
#   3. your best and worst day combined
combinedMinMax = (max(sales) + min(sales)) * 1.50
print(f"Your combined profit on your best day and worst day was ${combinedMinMax}.")
