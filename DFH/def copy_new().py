import pickle
def WRITEREC():
    f=open("ITEMS.dat","wb")
    while True:
        item_id=int(input("item id: "))
        item_name=input("item name: ")
        amount=int(input("amount: "))
        rec={item_id:[item_name,amount]}
        pickle.dump(rec,f)
        ch=input("More rec?(y/n)")
        if ch in 'Nn':
            break
    f.close()
def copy_new():
    f=open("ITEMS.dat","rb")
    f1=open("new_items.dat","wb")
    try:
        while True:
            data=pickle.load(f)
            for items_id,details in data.items():
                if details[1]>1000:
                    pickle.dump({items_id: details},f1)
                    print({items_id: details})
    except EOFError:
        f.close()
        f1.close()
#WRITEREC()
copy_new()
