f1=open(r"C:\Users\agrim\OneDrive\Desktop\vision.txt","r")
f2=open(r"C:\Users\agrim\OneDrive\Desktop\LOWER.txt","w")
f3=open(r"C:\Users\agrim\OneDrive\Desktop\UPPER.txt","w")
f4=open(r"C:\Users\agrim\OneDrive\Desktop\OTHERS.txt","w")
a=f1.read()
print(f1)
b=a.split()
for i in b:
    if i.isupper():
       f3.write(i) 
    elif i.islower():
        f2.write(i)
    elif i.isdigit():
        f4.write(i)
    elif i.isspace():
        f4.write(i)    
f1.close()
f2.close()
f3.close()
f4.close()
        
