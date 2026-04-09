# Declarar una super.lista con la siguiente informacion: 
# fila0 4 7 9 45
# fila1 1 5 6 3
# fila2 20 30 10 3
# fila3 7 15 3 477
# fila4 5 40 30 10
# Obtener aquellas filas donde haya un valor que sea múltiplo  de todos los valores nummericos que lees rodean (sin tener en cuenta el valor diagonal). En este ejemplo, en la fila 2 el valor 30.

super_lista= [
    ["fila0", 4, 7, 9, 45],
    ["fila1", 1, 5, 6, 3],
    ["fila2", 20, 30, 10, 3],
    ["fila3", 7, 15, 3, 477],
    ["fila4", 5, 40, 30, 10]
]

def es_multiplo_de_todos(super_lista, fila, col):
    valor = super_lista[fila][col]
    for i in range(max(0, fila-1), min(len(super_lista), fila+2)):
        for j in range(max(1, col-1), min(len(super_lista[i]), col+2)):
            if (i != fila or j != col) and super_lista[i][j] != 0:
                if valor % super_lista[i][j] != 0:
                    return False
    return True

filas_multiplo = []
for i in range(len(super_lista)):
    for j in range(1, len(super_lista[i])):
        if es_multiplo_de_todos(super_lista, i, j):
            filas_multiplo.append(super_lista[i])
            break

print("Filas con valores múltiplos de sus vecinos:", filas_multiplo)

