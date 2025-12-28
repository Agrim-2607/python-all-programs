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
while True:
    o=input("Enter the operation to be performed?(push/pop)")
    if o=='push':
        n=int(input("Enter the value to be appended"))
        stack.append(n)
    elif o=='pop':
        stack.pop()
    ch=input("Do you want to perform more operations?(y/n)")
    if ch=='n':
        break
print(stack)    
