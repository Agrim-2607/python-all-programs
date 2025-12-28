import pickle
def write():
    f=open("Sample.dat",'wb')
    record=[]
    while True:
        rno=int(input("Enter roll no:"))
        name=input("Enter name:")
        grade=input("Enter grade:")
        marks=int(input("Enter marks:"))
        data=[rno,name,grade,marks]
        record.append(data)
        ch=input("Do you want to add more reacords?(y/n)")
        if ch=="n":
            break
    pickle.dump(record,f)

def read():
    f=open("Sample.dat",'rb')
    s=pickle.load(f)
    for i in s:
        rno=i[0]
        name=i[1]
        grade=i[2]
        marks=i[3]
        print(rno,name,grade,marks)
    f.close()

def search():
    f=open("Sample.dat",'rb')
    s=pickle.load(f)
    for i in s:
        if i[3]>=50 and i[3]<=70:
            print("Displaying records having marks between 50 and 70:",i)

write()
read()
search()
