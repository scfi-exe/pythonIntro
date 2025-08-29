print("python101 - Enumerate")
friends = ["Brian", "Judith", "Reg", "Loretta", "Colin"]
count = 0

print("=== Without using Enumerate ===")
for friend in friends:
    count += 1
    print(f"{count}. {friend}")


print("=== With using Enumerate ===")
for num, friend in enumerate(friends, 51):
    print(num, friend)

print(" === Double-layered Enumeration ===")
for friend in enumerate(enumerate(friends, 51), -100):
    print(friend)

print("=== Enumerating a String ===")
for num, letter in enumerate("python", 5):
    print(num, letter)


shoppingList = ["bread", "milk", "eggs"]
for i in enumerate(shoppingList, 1):
    print(i)

print(type(enumerate(friends)))
print(list(enumerate(friends)))
