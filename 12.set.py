# Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed. (not itreatable)
a={'utsav','aman','vijaya'}
print(a)
print(type(a))
#duplicate is not allowed
a1={'utsav','aman','utsav'}
print(a1) #it will always return unique

#👉 true -1 and false -0 treated same value

#loop without index
for value in a1:
    print(value)

# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
a1.add('vijaya')
print(a1)

#remove item
        #remove
# a1.remove('utsav')
# a1.remove('utsav')  # if item is not available is through error for that reason we are using discard

# print(a1)
       #discard
# a1.discard('utsav')
# a1.discard('utsav')  # if item is not available also it is not throwning error

# print('discard',a1)
           #pop - it remove rancom item
# a1.pop()
# print(a1)
           #clear - it remove all item
# a1.clear()
# print(a1)
           #del - it is deleting directly set
# del a1
# print(a1)  //error a1 is not there

#union and intersect

a2={"utsav",'aman','vijaya'}
a3={'daksh','ved','vaau','utsav'}
result=a2.union(a3)
result2=a2.intersection(a3)
print(result)
print(result2)