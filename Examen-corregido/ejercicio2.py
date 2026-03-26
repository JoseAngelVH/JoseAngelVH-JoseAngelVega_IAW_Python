# Declarar una super-lista con listas que contienen valores numéricos. A partir de la super-lista, obtener uns lista A con la media de los valores que están en las posiciones impares en las sub-listas. Visualizar ls listaA.
# Ejemplo:
# 2,3,5,6,7,8
# 1,2,3,4,5,6,7,8
# 5,6,7,8
# lista: posición0: media de 3+2+6
#        posición1: media de 6+4+8
#        posición2: media de 8+6
#        posición3: media de 8

def calcular_media_posiciones_impares(super_lista):
    listaA = []
    for sublista in super_lista:
        suma_impares = 0
        contador_impares = 0
        for i in range(1, len(sublista), 2):  # Posiciones impares: 1, 3, 5, ...
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