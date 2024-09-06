class Company:
    def __init__(self,name="",add=""):
        self.name="anomus"
        self.add="unknow"
    def print_details(self):
        self.name="utsav"
        self.add="delhi"
        print(f"my name is {self.name} and {self.add}")

s1=Company()
s1.print_details()
