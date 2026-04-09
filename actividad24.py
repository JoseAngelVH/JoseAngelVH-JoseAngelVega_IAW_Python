# Declara una super lista de 3 filas y 4 columnas, obtener otra con la misma información pero de 4 filas y 3 columnas, pero si la columna tiene más de 3 elementos los siguiente tiene que ir en la siguiente fila. Con funciones.

superlistas = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

def cambiar_superlista(superlistas):
    nueva_superlista = []
    fila_actual = []
    for i in superlistas:
        for j in i:
            fila_actual.append(j)
            if len(fila_actual) == 3:
                nueva_superlista.append(fila_actual)
                fila_actual = []
    if fila_actual:
        nueva_superlista.append(fila_actual)
    
    return nueva_superlista

def Visualizar(dato):
    print(dato)

resul = cambiar_superlista(superlistas)
Visualizar(resul)
