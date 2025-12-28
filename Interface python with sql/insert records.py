import mysql.connector
con=mysql.connector.connect(host='localhost',
                                                user='admin',
                                                password='root',
                                                database='Bank')
cur=con.cursor()
while True:
    Accno=int(input("Account number: "))
    Cname=input("Candidate name: ")
    Atype=input("Account type: ")
    Amount=int(input("Amount: "))
    query="Insert into Bank_Account values(%s,'%s','%s',%s)"%(Accno,Cname,Atype,Amount)
    cur.execute(query)
    con.commit()
    ch=input("More records(Y/N)?")
    if ch in 'Nn':
        break
con.close()    
