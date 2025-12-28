# # Python doesn't support Method overloading-

# class Demo:
#     def add(self,a,b,c=0):
#         return a+b+c
# d=Demo()
# print(d.add(2,3))
# print(d.add(2,3,5))#here we are passing the value of 3rd parameter c and it is being over load. This is the same as method over loading


# class demo:
#     def add(self,*args): #*args means variable length arguements, mtlb u can give any number of values.
#         sum=0
#         for i in args:
#             sum+=i
#         return sum
# d=demo()
# print(d.add(2,3))
# print(d.add(2,3,5,10))
# print(d.add(2,3,5,10,16,28))

#Python does support Method overriding- 

class Father:
    def sleep(self):
        print("sleep 6 hrs")
    def eat(self):
        print("eating")
class Son(Father):
    def sleep(self):
        print("sleep 8 hrs")# now this is an example of method overriding 
Agrim=Son()
Agrim.sleep()