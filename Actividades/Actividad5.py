# Escribir una funcion que reciba una lista de listas (estas con dos valores cada una) 
# y que devuelva un diccionario en donde las claves sean los primeros elementos de las sublistas, 
# y los valores los segundos elementos de las sublistas.

lista = [["nombre", "Juan"], ["edad", 30], ["ciudad", "Madrid"]]

def lista_a_diccionario(lista):
    diccionario = {}
    for sublista in lista:
        if len(sublista) == 2:
            clave, valor = sublista
            diccionario[clave] = valor
    return diccionario

resultado = lista_a_diccionario(lista)  
print(resultado)