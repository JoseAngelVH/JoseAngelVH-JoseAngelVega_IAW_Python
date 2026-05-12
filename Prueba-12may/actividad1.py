# Declarar la siguiente información en una lista y diccionarios:
# A) Visualizar los nombres y suldo de los empleadosque cobren mas de 1500 euros
# B) Visualizar la media de los sueldo de los empleados de Hogar
# C) Visualizar el nombre y departamento del empleado/a que gane mas sueldo


lista =[
    {"nombre":"Antonio Gonzalez","sueldo":1500,"departamento":"Deportes"},
    {"nombre":"Maria Torres","sueldo":2500,"departamento":"Juegos"},
    {"nombre":"Javier Moreno","sueldo":2100,"departamento":"Hogar"},
    {"nombre":"Laura Moreno","sueldo":1900,"departamento":"Hogar"},
    {"nombre":"Luis Fernandez","sueldo":1700,"departamento":"Deportes"},
]

def mas1500(lista):
    for x in lista:
        if x ["sueldo"] > 1500:
            print("Nombre:", x["nombre"], "- Sueldo:", x["sueldo"])

mas1500(lista)

def mediahogar(lista):
    conta = 0
    suma = 0 
    for x in lista:
        if x ["departamento"] == "Hogar":
            conta += 1
            suma += x ["sueldo"]
    if conta > 0:
        media = suma / conta
        print("La media de empleados en hogar es:", media)
    else:
        print("No hay empleados en el departamento de hogar.")  

mediahogar(lista)

def masalto(lista):
    max_sueldo = 0
    empleado_mas_alto = None
    for x in lista:
        if x ["sueldo"] > max_sueldo:
            max_sueldo = x ["sueldo"]
            empleado_mas_alto = x
    if empleado_mas_alto:
        print("El empleado con el sueldo más alto es:", empleado_mas_alto["nombre"], "del departamento de", empleado_mas_alto["departamento"], "con un sueldo de", max_sueldo)
    else:
        print("No hay empleados en la lista.")

masalto(lista)