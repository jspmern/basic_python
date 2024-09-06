class Marks:
    def __init__(self,phy,eng,math):
        self.phy=phy
        self.eng=eng
        self.math=math
    @property
    def percentage(self):
        return str((self.phy +self.eng + self.math))
    
stu1=Marks(98,97,98)
stu1.phy=34
print(stu1.percentage)