def showinlines():
    f1=open("C:\\Users\\agrim\\OneDrive\\Desktop\\STORY1.txt","r")
    data=f1.read()
    for i in data:
        if i=='.' or i=='?' or i=='!':
            print(i, end='\n')
        else:
            print(i, end='')
    f1.close()    
showinlines()
