# Escribir una funcion  que reciba una lista de listas(conn dos valores cada una), y que devuelva un diiccionario en donde las claves seean los primeros elementos de  las listas y valores lossegundos elementos de las listas

def crear_diccionario(lista_de_listas):
    diccionario = {}
    for sublista in lista_de_listas:
        if len(sublista) == 2:
            clave = sublista[0]
            valor = sublista[1]
            diccionario[clave] = valor
    return diccionario

super_lista = [
    ["clave1", "valor1"],
    ["clave2", "valor2"],
    ["clave3", "valor3"],
    ["clave4", "valor4"]
]

resultado = crear_diccionario(super_lista)
print(resultado)    
    