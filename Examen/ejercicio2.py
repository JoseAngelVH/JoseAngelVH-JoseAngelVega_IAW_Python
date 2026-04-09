#Declarar una super-lista con listas que contienen valores numericos. A partir de la super-lista, obtener una lista A con la media de los valores que están en las posiciones impares en las sub-listas. Visualizarlaa lista A


def calcular_media_posiciones_impares(super_lista):
    listaA = []
    for sublista in super_lista:
        suma_impares = 0
        contador_impares = 0
        for i in range(1, len(sublista), 2):
            suma_impares += sublista[i]
            contador_impares += 1
        if contador_impares > 0:
            media = suma_impares / contador_impares
            listaA.append(media)
    return listaA

super_lista = [
    [2, 3, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [5, 6, 7, 8]
]

listaA = calcular_media_posiciones_impares(super_lista)
print("Lista A con la media de los valores en posiciones impares:", listaA)

