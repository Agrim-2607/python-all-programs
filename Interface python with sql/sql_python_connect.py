import mysql.connector
a=mysql.connector.connect(host="127.0.0.1", user="root", password="")
b=a.cursor
b.execute("create table VVS(Name char(20),  Class varchar(20), Roll_no numeric(20), Marks numeric(20))")
b.close()
a.close()
