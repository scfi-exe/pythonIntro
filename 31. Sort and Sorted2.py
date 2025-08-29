myList = [1, 5, -3, 7, -2]
listOfLists = [["car", 4, 65], ["dog", 2, 30], ["cat", 3, 10], ["bee", 1, 24]]

# sorting myList through absolute value
print(sorted(myList, key=abs))


# sorting a list of lists
print(sorted(listOfLists), "Default sorting for list of lists")
# by changing the value in :item[x], it will change which item in the list of lists we sort by
print(sorted(listOfLists, key=lambda item: item[2]))
