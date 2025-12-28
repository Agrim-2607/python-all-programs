import pickle
def WRITEREC():
    f=open("OFFICE.dat","wb")
    print("-----APPENDING RECORDS-----")
    while True:
        candidate_id=int(input("candidate id: "))
        candidate_name=input("candidate name: ")
        designation=input("designation: ")
        experience=float(input("experience in years: "))
        data=[candidate_id, candidate_name, designation, experience]
        pickle.dump(data,f)
        ch=input("More rec?(y/n)")
        if ch in 'Nn':
            break
    f.close()
def readNotSM():
    print("------DISPLAYING RECORDS who are not SM------")
    f=open("OFFICE.dat","rb")
    try:
        while True:
            data=pickle.load(f)
            if data[2]!='Senior Manager':
                print(data)
    except:
        f.close()    
def update():
    print("------UPDATING RECORDS exp>10------")
    f=open("Office.dat","rb")
    NL=[]
    try:
        while True:
            data=pickle.load(f)
            if data[3]>10:
                data[2]="Senior Manager"
                NL.append(data)
            else:
                NL.append(data)
    except:
        f.close()
    f=open("OFFICE.dat","wb")
    pickle.dump(NL,f)
    f.close()
def readAU():
    print("------READING RECORDS------")
    f=open("OFFICE.dat","rb")
    data=pickle.load(f)
    for i in data:
        print(i)
    f.close()    

#WRITEREC()
readNotSM()
update()
readAU()
    
