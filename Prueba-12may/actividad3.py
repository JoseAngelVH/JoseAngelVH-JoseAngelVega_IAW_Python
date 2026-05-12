# Se considera  una lista mat (4x5) (4 filas y 5 columnas) con los valores numéricos entero que estime el usuario.Con funciones
# A) Guardar en otra lista tab las sumas de cada una de las 4 filas
# B) Visualizar la lista tab de dos formas diferentes.
# C) Visualizar que fila tiene mayor suma, indicando con palabras: "primera","segunda","tercera" o "cuarta" (estos datos se almacenan en una tupla).

def Guardar():
    mat = []
    for i in range(4):
        fila = []
        for j in range(5):
            valor = int(input(f'Ingrese el valor para la posición ({i}, {j}): '))
            fila.append(valor)
        mat.append(fila)
    return mat

def Sumar_filas(mat):
    tab = []
    for fila in mat:
        suma = sum(fila)
        tab.append(suma)
    return tab

def Visualizar(tab):
    print("Suma de cada fila:")
    for i, suma in enumerate(tab):
        print(f"Fila {i + 1}: {suma}")

def Mayor_suma(tab):
    max_suma = max(tab)
    fila_mayor = tab.index(max_suma) + 1
    return fila_mayor, max_suma

mat = Guardar()
tab = Sumar_filas(mat)
Visualizar(tab)
fila_mayor, max_suma = Mayor_suma(tab)
print(f"La fila con mayor suma es la fila {fila_mayor} con una suma de {max_suma}.")