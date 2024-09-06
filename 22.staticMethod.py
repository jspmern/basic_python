#static method you can call , by using instance and class name 
class Student:
    def __init__(self,name):
        self.name=name

    def print_data(self):
        print(self.name)    

    @staticmethod
    def collageName():
        print('arya college of engnieering and it ,jaipur')
    
s1=Student('utsav')
s1.collageName()  #static method
s1.print_data()   #normal method
Student.collageName()
 
