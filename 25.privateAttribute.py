class Student:
    def __init__(self,name,add):
        self.__add=add
        self.name=name
    def __hello(self):
        print('hello i am private class')  
    def print1(self):
        self.__hello()


s1=Student('utsav','delhi')
print(s1.name)
#print(s1.__add)    
# s1.__hello() #we can't access outside
s1.print1()