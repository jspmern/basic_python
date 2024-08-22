
#Strings in python are surrounded by either single quotation marks, or double quotation marks or thriple quotation
# example  "utsav",'utsav'."""utsav """
name='utsav'
name1="utsav"
name2="""utsav"""
#print(name,type(name))
#print(name1,type(name))
#print(name2,type(name))

#by using \n and \t you can give next line and tab space
str="Hi,\n I am utsav form delhi\tand i am currently living in blr"
#print(str)

#indexing
str1="utsavkumarjha"
# print(str1[0])
# print(str1[2])
# print(str1[40])  #out of bound is not allowed

#👉 we can't assign the value (immutable)
#str1[1]='xx'
# print(str1)

#string length
str2="hello how are you"
#print(len(str2))

#concatenation
str3='utsav'
str4='jha'
result=str3+" "+str4
#print(result)

#slicing (it is not changing actual string)
str5='iamutsav'
r=str5[:5] #0-4
z=str5[1:5] #1-4
print(r)
print(z)
b = "Hello, World!" #negative indexing is also possible
print(b[-5:-2])

#upperCase
a = "Hello, World!"
print(a.upper())

#lowerCase
a1 = "Hello, World!"
print(a1.lower())

#The strip() method removes any whitespace from the beginning or the end:

a2 = " Hello, World! "
print(a2.strip()) # returns "Hello, World!"

# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# Example
# Create an f-string:

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)


# capitalize()	Converts the first character to upper case
a='utsav'
result=a.capitalize()
print(result)

#count
# Return the number of times the value "apple" appears in the string:

# txt = "I love apples, apple are my favorite fruit"

# x = txt.count("apple")
# print(x)

#https://www.w3schools.com/python/python_strings_methods.asp