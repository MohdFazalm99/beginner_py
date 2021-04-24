"""
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"r+" - Will allows user to read as well as write

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""

employee_Info = open("23(a)-users.csv", "r")

print(employee_Info.readable())
# Python File readable() Method
# The readable() method returns True if the file is readable, False if not.

print(employee_Info.readline())
# The readline() method returns one line from the file.
#
# You can also specified how many bytes from the line to return, by using the size parameter.

print(employee_Info.readline())

print(employee_Info.readlines()[2])
# The readlines() method returns a list containing each line in the file as a list item.
#
# Use the hint parameter to limit the number of lines returned. If the total number of bytes returned exceeds the specified number, no more lines are returned.
#                OR
"""for employee in employee_Info.readlines():
    print(employee)
    this for printing all the employee one by one"""

employee_Info.close()

