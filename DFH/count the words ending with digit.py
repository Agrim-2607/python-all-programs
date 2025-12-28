def count_Dwords():
    f=open("C:\\Users\\agrim\\OneDrive\\Desktop\\DETAILS.txt","r")
    data=f.read()
    words=data.split()
    count=0
    for word in words:
        if word[-1].isdigit() :
            count+=1
    print("Total no. of word ending with digit: "count)
    f.close()
count_Dwords()
