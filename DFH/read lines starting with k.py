def countlines():
    f=open(r"C:\Users\agrim\OneDrive\Desktop\agrim1.txt","r")
    l=f.readlines()
    c=0
    for i in l:
        if i[0]=="K" or i[0]=="k":
            c+=1
    print("Total number of lines starting with K:", c,":",i)
    f.close()
countlines()    
    
