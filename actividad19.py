#Crear una superlista que tenga en cada lista un nombre de empleado y sus diferentes ventas, tienes que obetner un diccionario en el que las clave sea el nombre y el valor sea ls lista de sus ventas. Hacer con funciones.

def crear_diccionario(superlista):
    diccionario = {}
    for sublista in superlista:
        nombre = sublista[0]
        ventas = sublista[1:]
        diccionario[nombre] = ventas
    return diccionario
superlista = [
    ["Jose", 100, 200, 150],
    ["Pepe", 300, 250, 400],
    ["Juan", 50, 75, 125]
]
diccionario_empleados = crear_diccionario(superlista)
print(diccionario_empleados)
