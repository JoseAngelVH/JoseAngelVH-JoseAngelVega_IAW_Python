# Introcducir valores numericos en una lista maximo 5 valores de forma ascendente  de forma que si el anterior es menor no se mete en la lista. El ejercicio tiene que estar realizado con funciones

def pedir_numeros():
    numeros = []
    while len(numeros) < 5:
        pedir = int(input("Introduce un valor numerico: "))
        if len(numeros) == 0 or pedir >= numeros[-1]:
            numeros.append(pedir)
        else:
            print("El valor debe ser mayor que el anterior.")
    return numeros

lista = pedir_numeros()
print("Lista final de los valores numericos:", lista)