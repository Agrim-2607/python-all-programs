import csv 
def write():
    f=open("items.csv","w",newline='')
    swriter=csv.writer(f)
    swriter.writerow(['INo','IName','Qty','Price'])
    rec=[]
    while True:
        n=int(input("Enter the item no:"))
        name=input("Enter the item name:")
        qty=int(input("Enter the item qty:"))
        price=int(input("Enter the price(in rs):"))
        data=[n,name,qty,price]
        rec.append(data)
        ch=input("Do you want to add more records?(y/n)")
        if ch=="n":
            break
    swriter.writerows(rec)
    f.close()
#write()

def read():
    f=open("items.csv","r",newline='')
    print("Reading data from csv file:")
    sreader=csv.reader(f)
    for i in sreader:
        n=i[0]
        name=[1]
        qty=i[2]
        price=i[3]
        print(i)
read()

def search():
    f=open("items.csv","r")
    print("Searching data from a csv file..")
    s=input("Enter the item no to be searched:")
    sreader=csv.reader(f)
    for i in sreader:
        if i[0]==s:
            print(i)
        else:
            print("The record doesn't exist")
    f.close()
search()    
    
    
    
     
