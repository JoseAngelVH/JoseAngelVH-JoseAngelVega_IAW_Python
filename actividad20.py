# Declarar una super-lista con la siguiente información:
# fila0 4 7 9 45
# fila1 1 5 6 3
# fila2 20 30 10 3
# fila3 7 15 3 477
# fila4 5 40 30 10
# Visualizar el nombre de la fila en el que la media sea mayor de 10

superlista=[
    ["fila0", 4, 7, 9, 45],
    ["fila1", 1, 5, 6, 3],
    ["fila2", 20, 30, 10, 3],
    ["fila3", 7, 15, 3, 477],
    ["fila4", 5, 40, 30, 10]
]

def Visualizar(superlista):
    for lista in superlista:
        media = Media(lista)
        if media > 10:
            print(lista[0])

def Media(lista):
    suma = 0
    for i in range(1, len(lista)):
        suma += lista[i]
    media = suma / (len(lista) - 1)
    return media

Visualizar(superlista)
