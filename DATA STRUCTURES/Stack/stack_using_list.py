#1
'''
l=list(input("enter the values"))
while True:
    n=input("Enter the values to be inserted")
    l.append(n)
    ch=input("Do you want to add more values?(y/n)")
    if ch=='n':
        break
print(l)    
'''   
#2
#l=list(input("Enter the values:"))
stack=[]
choice='y'
while choice=='y':
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    c=int(input("Enter your choice:"))
    if c==1:
        n=int(input("Enter the value to be appended"))
        stack.append(n)
    elif c==2:
        if stack==[]:
            print("stack is empty...underflow")
        else:
            print("Deleted element:",stack.pop())
    elif c==3:
         for i in range(len(stack)-1,-1,-1):
             print(stack[i])
    else:
        print("wrong input")
    choice=input("Do you want to perform more operations?(y/n)")
    if choice=='n':
             break
   
