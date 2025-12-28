class Human: #parent class
     # def __init__(self, num_heart):
     #      self.num_heart=num_heart #if i pass an arguement in the parent class then wehn i will try to access the attributes of this class in the child class it will give an error inspite of using the super fnc bcz we will have to pass the agruemnt there also
     def __init__(self): 
          self.no_eyes=2
     def eat(self):
           print("Human can eat")
     def sleep(self):
           print("Human can sleep")
class Male(Human):  #child class/deprived class
    #instead of rewriting the same attributes as in parents class we can inherit them into child class
     #def __init__(self, heart):
          #super().__init__("Agrim"/2)'''if i directly pass a data as a parameter then it will return None'''
          #super().__init__(heart)# ye chl ni rha h idk why but hota ye h ki humein basically number of parameter and arguements match krne k liye child class k def func or super func dono mein parameters and arguements dene pdte h or fir uski value obj call krte time deni hoti h
     def __init__(self,name):
          self.name=name
     def workout(self):
           print("male can workut")
     def eat(self):
           print("I can eat more") # method overriding- parent class k method ko override krwa diya
           super().eat() # par meko toh dono print krne the parent class ka method bhi aur child class ka bhi
     def display(self):
          #print(f"Hi my name is {self.name}")#for fetching the attributes of any class inside the print func using f string
           print("Hi my name is", self.name)#for fetching the attributes of any class inside the print func 

male_1=Male("Agrim")
#male_1.sleep()
#male_1.eat()
#male_1.workout()
#print(male_1.no_eyes)# iss case mein ye isliye ni chlega bcz init function ab Male class mein bhi h, jismein no_eyes krke koi attribute ya variable declared nhi h
#par still agr mujhe voh attribute access krna h toh i have to use super fnc with the name of that fnc whose attribute i want to access for eg: super().__init__()
#print(male_1.__init__())
male_1.display()