import mysql.connector
con=mysql.connector.connect(host='localhost',
                                                user='root',
                                                password='Pencil',
                                                database='itemdb')
cur=con.cursor()
def ADDANDDISPLAY():
    while True:
        itemNo=int(input("item no: "))
        itemName=input("name of the item: ")
        price=int(input("item name: "))
        qty=int(input("item quantity: "))
        query="Insert into STATIONARY values(%s,'%s',%s,%s)"%(itemNo,itemName,price,qty)
        cur.execute(query)
        con.commit()
        print("Data inserted succesfully")
        ch=input("More rec(Y/N)?")
        if ch in 'Nn':
            break
        cur.execute("Select * from STATIONARY where price>120")
        data=cur.fetchall()
        for i in data:
            print(i)
ADDANDDISPLAY()
con.close()
