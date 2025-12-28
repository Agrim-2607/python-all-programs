class complexnumbers:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    # def __add__(self,other):
    #     return f"{self.real+other.real}+{self.imaginary+other.imaginary}i" # another method of adding two values of two seperate objects respectively
c1=complexnumbers(1,2)
c2=complexnumbers(4,5)
r=c1.real+c2.real
i=c1.imaginary+c2.imaginary
print(f"{r}+{i}i")
  
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        if self.age>other.age:
            return True
        else:
            return False
p1=Person("Ram", 32)
p2=Person("Shyam", 23)
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")