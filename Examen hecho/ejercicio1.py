#Pedir por teclado hasta que sea hayaan tecleados 8 valores multiplos de 7. Visulizar los 8 valoress anteriores múltiplos de 7 y visualizar, de los 8 valores anteriores múltiplos de 7, solo los valores pares pero en orden inverso al teclado.

def obtener_multiplos_de_7():
    multiplos_de_7 = []
    while len(multiplos_de_7) < 8:
        valor = int(input("Ingrese un valor múltiplo de 7: "))
        if valor % 7 == 0:
            multiplos_de_7.append(valor)
        else:
            print("El valor ingresado no es múltiplo de 7. Intente nuevamente.")
    return multiplos_de_7

multiplos_de_7 = obtener_multiplos_de_7()
print("Los 8 valores múltiplos de 7 ingresados son:", multiplos_de_7)
    
