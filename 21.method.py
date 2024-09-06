class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_data(self):
        return f"{self.name}  {self.age}"
    def print_data2(self):
        print('hello how are you')

s1=Student('utsav',23)
s1.print_data2()
print(s1.print_data())
        