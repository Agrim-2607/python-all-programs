import pickle
def WRITEREC():
    f=open("SPORT.dat","wb")
    while True:
        SportName=input("Sport Name: ")
        TeamName=input("Team name: ")
        No_Players=int(input("No. of players: "))
        rec=[SportName,TeamName,No_Players]
        pickle.dump(rec,f)
        ch=input("More rec?(y/n)")
        if ch in 'Nn':
            break
    f.close()
def copydata():
    f=open("SPORT.dat","rb")
    f1=open("BASKET.dat","wb")
    count=0
    try:
        while True:
            data=pickle.load(f)
            if data[0]=="Basketball":
                pickle.dump(data,f1)
                print(data)
                count+=1
    except:
        f.close()
    return count
#WRITEREC()
print("Total number of records with basketball as sports name:", copydata())n
    
            
    
    
