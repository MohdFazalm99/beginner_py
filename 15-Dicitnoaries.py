# Dictionary
# Dictionaries are used to store data values in key:value pairs.
#
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# Example 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

# Month Conversion

monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    8: "August"

}

print(monthConversion["Jan"])
# Here we are getting the value using the keys, here for fetching the value we are using [] brackets

print((monthConversion.get("Apr")))
# Here in the 2nd example we are fetching the value of April using the .get() function

print(monthConversion.get("Dec"))
# Here in the above example when we are fetching a value which is not in the dictionary we will get "None"

print(monthConversion.get("Dec", "December"))
# Here in the above example we are giving a default key value pair which is not in the dictionary

print(monthConversion[8])
# Here in the above example we are getting a value by using a numeric key
