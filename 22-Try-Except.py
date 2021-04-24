# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#
# These exceptions can be handled using the try statement:

"""
The try block lets you test a block of code for errors.

The except block lets you handle the error. It is similar to the catch in java where it catch any error in the program and run the program under it.
In this we have to specify which type of error you want to run otherwise if it sees any error it will automatically print the error message.
Exampl1 will demonstrate the above situation

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# Example 1
try:
    value = 10 / 0
    num = int(input(" Enter the number : "))
except:
    print("Invalid Number")

# here in the example1 we see that  we didn't get the chance to enter the number as when the except block sees that 10/0 is an error it print the Invalid message although we assigned it for the user to enter the wrong input.
# on thing more except is showing "too broad exception clause" which means every error will be cached by it. Therefore we have to specify which type of error we want to handle

# Example 2

try:
    val = 10/0
    number = int(input("Enter the number : "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
# Here we already specify that which error we want to print
