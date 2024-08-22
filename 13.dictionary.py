
# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
details={
    "name":"utsav",
    "add":"delhi",
    "phone":6350068824,
    "gender":"male",
}
print(details)
# 👉 if key is same than its override with updated one.

#access
print(details["phone"])
         #or
print(details.get('add'))

#length
print(len(details))

#get keys
print(details.keys())

#get values
print(details.values())

#item    - The items() method will return each item in a dictionary, as tuples in a list.
print(details.items())


#update
details['sal']=100000
      #or
details.update({"name":"sidhu"})
print(details)


#remove
   #pop()
details.pop('sal')
print(details)
   #popitem() -it delete item form last
details.popitem()
print(details)
    #clear() -clear all dictionary item
details.clear()
print(details)

#copy - new reference
mydata=details.copy()
print(mydata==details)

#nested dictionary
a={
    "name":'utsav',
    "age":23,
    "add":{
        "pa":"delhi",
        "ca":'blr'
    }
}
print(a['add']['pa'])
