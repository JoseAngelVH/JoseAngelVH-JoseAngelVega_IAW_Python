# Dada una super-lista (lista de listas), por cada lista, anular todos los valores impares que se repitan. 
# Visualizarla super-lista modificada.

def anular_impares_repetidos(super_lista):
    for sublista in super_lista:
        impares_vistos = set()
        for i in range(len(sublista)):
            if sublista[i] % 2 != 0:
                if sublista[i] in impares_vistos:
                    sublista[i] = 0
                else:
                    impares_vistos.add(sublista[i])
    return super_lista

super_lista = [
    [1, 2, 3, 4, 5, 1],
    [6, 7, 8, 9, 7],
    [10, 11, 12, 13, 11, 10]
]

super_lista_modificada = anular_impares_repetidos(super_lista)
print(super_lista_modificada)
