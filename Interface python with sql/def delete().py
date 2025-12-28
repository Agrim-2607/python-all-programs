import mysql.connector
con=mysql.connector.connect(host="localhost",
                                                user="root",
                                                password="job",
                                                database="Agency")
cur=con.cursor()
cur.execute("Delete from Placement where CName='Raman'")
con.commit()
con.close()
