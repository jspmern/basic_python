# class Student:
#     name="utsav2333"
#     def __init__(self,age,add):
#         self.age=age
#         self.add=add
#     def deltails(self):
#         self.name="xyzzz"
# s1=Student(8,'delhi')
# s1.deltails()
# print(s1.name)
# print(Student.name)

class Student:
    name="utsav kumar jha"
    def __init__(self,age):
        self.age=age
    @classmethod
    def changeVarible(cls,name):
        cls.name=name

s1=Student(20)
Student.changeVarible('aman kumar jha')
print(s1.name)
print(Student.name)