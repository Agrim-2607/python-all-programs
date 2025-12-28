import csv
def Add_details():
    f=open("Sports.csv","w",newline='')
    wo=csv.writer(f)
    wo.writerow(["sports_id","competition","prize_won"])
    while True:
        s=int(input("Enter the sport id: "))
        c=input("Enter the competition name: ")
        p=input("Enter the prize won(gold,silver,bronze): " )
        rec=[s,c,p]
        wo.writerow(rec)
        ch=input("Do you want to enter more records?(y/n)")
        if ch in "Nn":
            break
    f.close()
def read():
    f=open("Sports.csv","r")
    ro=csv.reader(f)
    for i in ro:
        print(i)
    f.close()
def count_medal():
    f=open("Sports.csv","r")
    ro=csv.reader(f)
    next(ro)
    for i in ro:
        if i[2] in 'Goldgold':
            print(i[1])
    f.close()
#Add_details()
#read()
count_medal()















