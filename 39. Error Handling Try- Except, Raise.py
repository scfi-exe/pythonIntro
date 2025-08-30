try:
    num = int(input("Enter a number: "))
    if num > 30:
        raise ValueError(num)
except ValueError as err:
    print(f"{err}: Bad Value!")
except ZeroDivisionError as err:
    print(f"{err}: You can't divide by zero!")
except:
    print("Invalid Input!")
else:
    print("30 divided by", num, "is: ", 30 / num)
finally:
    print("**Thank you for playing!**")


# try:
# code you want to run
# except:
# executed if error occurs
# else:
# executed if no error
# finally:
# always executed
