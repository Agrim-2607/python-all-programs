class Mother:
    def __init__(self):
        self.no_eyes=2
        self.no_nose=1
    def cook(self):
        print("i can cook")
    def work(self):
        print("i can clean")

class Father:
    def __init__(self,no_ears):
        self.no_ears=no_ears
    def workout(self):
        print("i can workout")
    def work(self):
        print("i can earn")

class boy(Mother, Father):
    def __init_(self,no_ears=2):
        Mother.__init__(self)
        Father.__init__(self,no_ears=2)# if i want to acces the attribute from Father class then i need to specify the init function in boy class
    def work(self):
        print("i can sleep")

name=boy()
# name.cook()
# name.workout()
# name.work()
#print(boy.mro())# Method Resolution order #if the same fucntion is present in all the classes then first it wil serch for it in the primary/child class, then the order wil go acc to the order of arguements in which the classes names are written 
print(name.no_ears)