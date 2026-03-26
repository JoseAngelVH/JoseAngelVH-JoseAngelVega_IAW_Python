# Almacenar en un diccionario un vehiculo que contenga numero de matricula y su precio
# Preguntar al usuario  por un precio, devolver una array con aquellas matrices de aquellos
# coches con precio superior al introducido. En ejercico tiene que ser con funciones.

coche = {
    "1234 ABC": 4000,
    "5678 DEF": 8000,
    "9123 GHI": 6000,
    "4567 JKL": 2000
}

pedir_precio = float(input('Introduce el precio: '))

def precio_coche(coche, pedir_precio):
    tab=[]
    for matricula, precio in coche.items():
        if precio > pedir_precio:
            tab.append(matricula)
    return tab
print(precio_coche(coche, pedir_precio))
    


