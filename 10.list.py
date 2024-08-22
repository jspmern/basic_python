# List
# Lists are used to store multiple items in a single variable.
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

#  List Length
#To determine how many items a list has, use the len() function:

#Acess
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

#change item value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

#change range item value
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

#insert Item : To insert a list item at a specified index, use the insert() method.
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

#To add an item to the end of the list, use the append() method:

#Extend List
# To append elements from another list to the current list, use the extend() method.

# Example
# Add the elements of tropical to thislist:

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# Remove Specified Item
# The remove() method removes the specified item.

# ExampleGet your own Python Server
# Remove "banana":

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# Remove Specified Index
# The pop() method removes the specified index.

# Example
# Remove the second item:

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)


# The clear() method empties the list.

# The list still remains, but it has no content.

# Example
# Clear the list content:

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)