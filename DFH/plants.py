import pickle
def WRITEREC():
    f=open("Plants.dat","wb")
    while True:
        ID=int(input("Plant id: "))
        NAME=input("Plant name: ")
        PRICE=int(input("Plant price: "))
        rec=[ID,NAME,PRICE]
        pickle.dump(rec,f)
        ch=input("More rec?(y/n)")
        if ch in 'Nn':
            break
    f.close()
def SHOWHIGH():
    f=open("Plants.dat","rb")
    try:
        while True:
            data=pickle.load(f)
            if data[2]>500:
                print(data)
#            else:
#                print(data)
    except:
        f.close()    
#WRITEREC()
SHOWHIGH()
