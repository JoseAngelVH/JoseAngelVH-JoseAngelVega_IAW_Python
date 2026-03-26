import mysql.connector

conexion1=mysql.connector.connect(host="localhost", port=3307, user="root", passwd="")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base[0])
conexion1.close()   