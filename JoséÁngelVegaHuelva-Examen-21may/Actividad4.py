# Escribir una función que reciba una lista de listas (estas con dos valores cada una) 
# y que devuelva un diccionario en donde las claves sean los primeros elementos de las sublistas, 
# y los valores los segudos elementos de las sublistas.

lista = [["Nombre", "Jose"], ["Edad", 19], ["Ciudad", "Chiclana"]]

def lista_diccionario(lista):
    diccionario = {}
    for sublista in lista:
        if len(sublista) == 2:
            clave, valor = sublista
            diccionario[clave] = valor
    return diccionario

resultado = lista_diccionario(lista)  
print(resultado)