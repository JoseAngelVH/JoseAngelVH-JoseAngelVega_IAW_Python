# Declarar una lista con valores numericos enteros. Visualizar una tercera lista suma de los anteriores listas

class Numeros:
    def __init__(self, lista):
        self.lista = lista

    def __add__(self, lista_segunda):
        datos3 = []
        for i in range(len(self.lista)):
            datos3.append(self.lista[i] + lista_segunda.lista[i])
        return Numeros(datos3)
    
    def __str__(self):
        return f"{self.lista}"

datos1 = [3,8,0,7,9,5,1]
datos2 = [9,3,4,55,2,8,6]

obj1 = Numeros(datos1)
obj2 = Numeros(datos2)

obj3 = obj1 + obj2
print(obj3)

