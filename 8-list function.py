lucky_num = [1,22,33,444,555,633,6554]
friends = ["Shazeb","Abid", "Deepak", "Iffu"]
fr2 = ["hamza", "hammad", "Arham"]

friends.extend(lucky_num)
print(friends)
# extend function will add all the items of one list to another list

lucky_num.append(fr2)
print(lucky_num)
# append item will always add the new item at last of the list

friends.insert(1,fr2)
print(friends)

friends.insert(2,"Fazal")
print(friends)


fr2.remove("hammad")
print(fr2)

lucky_num.clear()
print(lucky_num)
# clear function will clear all the items in the list and print the empty list


friends.pop(3)
print(friends)

fr2.sort()
print(fr2)



