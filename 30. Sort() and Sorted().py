# lists and dicts are mutable
my_list = [1, 5, 3, 7, 2]
my_dict = {"car": 4, "dog": 2, "add": 3, "bee": 1}

# tuples and strings are not
my_tuple = ("d", "c", "e", "a", "b")
my_string = "python"

print(my_list, "original")
# .sort() can only be used with LISTS
# it sorts the list in-place, meaning it modifies the original list directly and does not return a new list
# it returns None on print()
print(my_list.sort())
# but now if we print my_list, we will get the sorted version
print(my_list, "new, using .sort()")


# sorted() is a built-in function that works on LISTS, TUPLES, STRINGS, DICTS, etc.
# it returns a new sorted list, and leaves the original iterable unchanges
print("=== SORTED ===")
my_list = [1, 5, 3, 7, 2]
print(my_list, "unsorted")
print(sorted(my_list), "sorted using .sorted()")
print(my_list, "original list stays unmodified as a variable")

print("=== SORTED DICTS ===")
# if we juts run sorted(dict), we will lose  a lot of information
print(sorted(my_dict))
# if we sort dict.items() instead, we will get the dict values as tuples inside of a list
print(sorted(my_dict.items()))
print(sorted(my_dict.items(), reverse=True))

# we can use a slicing syntax to reverse a list
print(my_list[::-1])
