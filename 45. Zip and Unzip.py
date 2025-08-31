nums = [1, 2, 3, 4]
letters = ["a", "b", "c", "d"]
names = ["John", "Marc", "Eric", "Rountree"]

zipTest = zip(nums, letters)
print(zipTest)  # printing the zip itself doesn't do much, we have to print it as a list
print(list(zipTest))  # listing the zip returns a list of tuples

nums = "1234"
zipTest = list(zip(nums, letters))
print(
    (zipTest)
)  # although we switch num to a string instead of 4 integers, we can still iterate over it -> the output changes


print(dict(zip(nums, letters)))

nums, letters = zip(
    *zipTest
)  # we're assigning the results of the unzip to 2 variables: nums, letters

print(nums, letters)
