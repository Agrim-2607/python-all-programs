f=open(r"C:\Users\agrim\OneDrive\Desktop\STORY.TXT","r")
a=f.read()
b=a.split()
c=0
d=[]
for i in range(len(b)):
    if len(b[i])<4:
        d.append(b[i])
        c+=1
print("Total no. of words less than 4 char:", c,"=", d)
f.close()            

