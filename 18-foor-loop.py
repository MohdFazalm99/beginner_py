
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Example 1)

for letters in "Fazal Mahmood":
    print(letters)

# Example 2)

friends = ["Abid","Iffu","Deepak"]
for name in friends:
    print(name)

# Example 2(b)
for index in range(len(friends)):
    print(friends[index], end=',')

# Example 3)

for index in range(10):
    print(index)



# Example 4)
for i in range(15):
    if i < 14 :
        print(i, end=',')
    else:
        print(i)


# Example 5)

for i in range(4,10):
    print(i, end=',')