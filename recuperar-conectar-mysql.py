import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1",
                                  port=3307)
cursor1=conexion1.cursor()
cursor1.execute("select codigo, descripción, precio from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()   