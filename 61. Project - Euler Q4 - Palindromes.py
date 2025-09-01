# project Euler #4 - largest palindrome of two 3 - digit numbers
# a palindrome is a number that is the same backwards and forwards, like 101 or 990099

import time

# find all palindromes between 100 and 999, so we need a fxn to determine if a # is a palindrome or not


def isPalindrome(val):
    val = str(val)
    if val == val[::-1]:
        return True
    else:
        return False


# another way to write the isPalindrome function, both work
# def isPalindrome(val):
#     return str(val) == str(val)[::-1]


def palindrome():
    startTime = time.time()
    palindromeList = []
    debugList = []
    lowVal = 100
    highVal = 999
    lowNum2Val = 900
    iterations = 0
    # for all numbers up to 999
    for num1 in range(highVal, lowVal, -1):
        if num1 < lowVal:
            break
        for num2 in range(highVal, lowNum2Val, -1):
            iterations = iterations + 1
            if isPalindrome(num1 * num2):
                palindromeList.append(num1 * num2)
                lowVal = max((num1 * num2) / highVal, lowVal)

                debugList.append([num1, num2, (num1 * num2) / highVal, lowVal])
            if num1 == num2:
                break
    print("Print of Palindromes: ", palindromeList, num1, num2)
    print("Debug List: ", debugList)
    print("Iterations: ", iterations)
    print(f"Largest Palindrome: {max(palindromeList)}")
    print(f"Runtime: {time.time()-startTime}")
    print("=== END RUN ===")


palindrome()
