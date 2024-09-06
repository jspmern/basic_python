class Addition :
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,s):
         self.real=s.real+self.real
         self.img=s.img+self.img
         return f"{self.real} i + {self.img} j"
    def __sub__(self,s):
         self.real=s.real-self.real
         self.img=s.img-self.img
         return f"{self.real} i + {self.img} j"
    def __mul__(self,s):
         self.real=s.real*self.real
         self.img=s.img*self.img
         return f"{self.real} i + {self.img} j"
s1=Addition(2,4)
s2=Addition(3,4)
#s3=s1+s2
#s4=s1-s2
s5=s1*s2
#print(s3)
#print(s4)
print(s5)
