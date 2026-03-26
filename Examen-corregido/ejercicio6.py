# Escribir una funcion que reciba una lista de listas con dos valores cada una, y que devuelva un diccionario en 
# donde las claves sean los primeros elementos de las listas y valores los segundos elementos de las listas

super_lista = [
    ["clave1", "valor1"],
    ["clave2", "valor2"],
    ["clave3", "valor3"],
    ["clave4", "valor4"]
]

def proceso(lista_de_listas):
    dic = {}
    for sublista in lista_de_listas:
            clave = sublista[0]
            valor = sublista[1]
            dic[clave] = valor
    return dic

result = proceso(super_lista)
print(result)