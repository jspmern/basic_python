class Student:
    def __init__(self,name,add):
        self.name=name
        self.add=add
    
s1=Student('utsav','delhi')
print(s1.name)

del s1.name
print(s1.name)