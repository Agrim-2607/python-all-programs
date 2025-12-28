file=open(r"C:\Users\agrim\OneDrive\Desktop\vision.txt","r")
handler=file.read()
count=0
for j in range(len(handler)):
    if "i" in (handler[j]):
        count+=1
print(count)
