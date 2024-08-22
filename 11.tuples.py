# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.
# a=('utsav','aman','vijaya','utsav')
# print(a)
# #lemgth
# print(len(a))

#Create Tuple With One Item
b=('utsav')   #if single item is there and if you want to create tuple like this , it is treated as a str for that one we have to use comma
# print(type(b))
# c=('utsav',)
# print(type(c))

#access tuples
a=('utsav','aman')
print(a[0])

#Check if Item Exists
if "utsav" in a:
    print('yes availabele')
else:
    print('not available')

# 👉tuple are immutable if you want to modify just convert into list and apply method and ageain convert into tuple
a1=('utsav','aman','ram')
#a1[2]='hello'  //error you can not modify
#a1.append('shyam') //can not  insert
y=list(a1)
y.append('shyam')
a1=tuple(y)
print(a1)

#loop in tuples
for x in a1:
    print(x,end=" ") #this is for same line

#loop through index no
for i in range(len(a1)):
    print(a1[i])
