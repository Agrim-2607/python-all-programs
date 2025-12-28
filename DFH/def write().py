import csv
def write():
    f=open("Happiness.csv","w",newline='')
    wo=csv.writer(f)
    wo.writerow(["Country","Population","Same Size","Happy"])
    while True:
        C=input("Enter the names of the country: ")
        P=int(input("Enter the population of the country: "))
        SS=int(input("Enter the Sampe size: " ))
        H=int(input("Enter the population that accepts that they are happy:"))
        rec=[C,P,SS,H]
        wo.writerow(rec)
        ch=input("Do you want to enter more records?(y/n)")
        if ch in "Nn":
            break
    f.close()
def read():
    f=open("Happiness.csv","r")
    ro=csv.reader(f)
    for i in ro:
        print(i)
    f.close()
def show():
    f=open("Happiness.csv", "r")
    ro=csv.reader(f)
    print(next(ro))
    for i in ro:
        if int(i[1])>5000000:
            print(i)
    f.close()
def count():
    f=open("Happiness.csv","r")
    ro=csv.reader(f)
    count=0
    next(ro)
    for i in ro:
        count+=1
    print("Total records: ",count)    
write()
read()
show()
count()








