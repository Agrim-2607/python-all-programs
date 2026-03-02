BigNums=[]
def PushBig():
    for i in Num:
        if len(str(i))>=5:
            BigNums.append(i)
def PopBig():
    while True:
        if BigNums==[]:
            print("Stack Empty")
            break
        else:
            print(BigNums.pop())
Num=[213,10025,167,254923,14,1297653,31498,386,92765]
PushBig()
print(BigNums)
PopBig()

    
