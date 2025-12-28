import mysql.connector
con=mysql.connector.connect(host='localhost',
                                                user='admin',
                                                password='Shopping',
                                                database='Keeper')
cur=con.cursor()
cur.execute("Update shop set Qty=20 where Item_code=111")
cur.commit()
con.close()
