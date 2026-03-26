#Crear una super lista, en la que contenga 5 listas, cada una de esas sublistas, se crean igual que en el ejercicio anterior (Actividad 16)

def pedir_numeros():
    numeros = []
    while len(numeros) < 5:
        pedir = int(input("Introduce un valor numerico: "))
        if len(numeros) == 0 or pedir >= numeros[-1]:
            numeros.append(pedir)
        else:
            print("El valor debe ser mayor que el anterior.")
    return numeros

superlista = []
for i in range(5):
    print(f"Introduce los numeros para la sublista {i + 1}:")
    sublista = pedir_numeros()
    superlista.append(sublista)

print("La superlista es:", superlista)

