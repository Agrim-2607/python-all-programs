f=open(r"C:\Users\agrim\OneDrive\Desktop\vision.txt","r")
a=f.read()
print(a)
l=len(a)
dig=alpha=sym=space=0
for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        alpha+=1
    elif i.isspace():
        space+=1
sym=l-(dig+sym+alpha+space)        
print("No. of digit:", dig)
print("No. of alphabets:", alpha)
print("No. of symbols:", sym)
f.close()
