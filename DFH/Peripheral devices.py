 import csv
def Add_devices():
    f=open("Peripheral.csv","w", newline='')
    wo=csv.writer(f)
    wo.writerow(["P_id","P_name","Price"])
    while True:
        pi=int(input("Enter the device id: "))
        pn=input("Enter the device name:")
        price=int(input("Enter the price: "))
        rec=[pi,pn,price]
        wo.writerow(rec)
        ch=input("Do you want to add more records?(y/n)")
        if ch in 'Nn':
            break
    f.close()
def read():
    f=open("Peripheral.csv","r")
    ro=csv.reader(f)
    for i in ro:
        print(i)
    f.close()
def count_devices():
    f=open("Peripheral.csv","r")
    ro=csv.reader(f)
    count=0
    print(next(ro))
    for i in ro:
        if int(i[2])<1000:
            count+=1
    print("No. of Device who's price is less than 1000=", count)
    print("Device who's price is less than 1000=", i)
    f.close()
#Add_devices()
read()
count_devices()
