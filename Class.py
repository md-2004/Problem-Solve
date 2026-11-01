class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)

S=student('mayuresh',"22")
S.display()