# Declarar una super-lista con la siguiente información:
# fila0 4 7 9 45
# fila1 1 5 6 3
# fila2 20 30 10 3
# fila3 7 15 3 477
# fila4 5 40 30 10
# Visualizar la media de los valores que no estan en el contorno, teniedo en cuenta que la posicion 0 es el nombre de la fila

superlista=[
    ["fila0", 4, 7, 9, 45],
    ["fila1", 1, 5, 5, 3],
    ["fila2", 20, 5, 5, 3],
    ["fila3", 7, 5, 5, 477],
    ["fila4", 5, 40, 30, 10]
]

def Visualizar(superlista):
    suma = 0
    contador = 0
    for i in range(1, len(superlista)-1):
        for j in range(2, len(superlista[i])-1):
            suma += superlista[i][j]
            contador += 1
    if contador > 0:
        media = suma / contador
        print(f"La media es: {media}")

Visualizar(superlista)
