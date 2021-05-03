"""
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content also we can create a new file by just naming it .
"""

emploee_file = open("24(a)-user.txt","a")

emploee_file.write("\nShazeb - Customer services")

emploee_file.close()