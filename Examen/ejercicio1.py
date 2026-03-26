# Pedir un numero por teclado hasta que se hayan tecleado 8 valores multiplo de 7. Visualizar los 8 valores multiplo de 7. 
# Visualizar de los 8 valores multiplo de 7 todos los valores pares en orden inverso tecleado

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
    
