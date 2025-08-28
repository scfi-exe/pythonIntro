# hree loop questions
# 1. What do I want to repeat? ---> the message
# 2. What do I want to change each time? ---> the stars
# 3. How many times should we repeat? ---> 5 times

count = 1
stars = "*"

while count <= 5:
    print(f"{count}.{stars*count}Loops are great{stars*count}")
    # this is basically the same as saying 'count = count+1'
    count += 1
