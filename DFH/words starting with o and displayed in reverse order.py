def RevString():
    f=open("C:\\Users\\agrim\\OneDrive\\Desktop\\INPUT.txt","r")
    data=f.read()
    words=data.split()
    for i in words:
        if i.startswith("O"):
            i=i[::-1]
        print(i, end=' ')
    f.close()
RevString()

