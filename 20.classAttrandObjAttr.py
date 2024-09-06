class Student:
     cllz_name="ACEIT,JAIPUR"   #class attribute
     def __init__(self,name):
          self.name=name         #object attribute

s1=Student('utsav')
print(s1.name)
print(s1.cllz_name)
print(Student.cllz_name)
          