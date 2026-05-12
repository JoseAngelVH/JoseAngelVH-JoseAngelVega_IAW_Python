# Almacenar números en una lista, desde el teclado, hasta que el valor teclado sea -99 (este no se guarde). 
# Visualizar los valores tecleados en orden inverso al tecleado.
# Con funciones.

numeros = []

def almacenar_numeros(numeros):
    sw = 0
    while (sw == 0):
        numero = int(input("Introduce un número (o -99 para terminar): "))
        if numero == -99:
            sw = 1
        else:
            numeros.append(numero)
    return numeros

def Visualizar(numeros_tecleados):
    print("Los números tecleados en orden inverso son:", numeros_tecleados[::-1])

numeros_tecleados = almacenar_numeros(numeros)
Visualizar(numeros_tecleados)
