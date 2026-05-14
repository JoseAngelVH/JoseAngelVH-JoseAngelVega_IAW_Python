# Declarar una lista con valores numericos enteros. Visualizar el mayor.


class mayor:
    def __init__(self, lista):
        self.lista = lista

    def mayor(self):
        mayor = max(self.lista)
        return mayor

lista1 = [3,8,0,7,9,5,1]
lista2 = [9,3,4,55,2,8]

lista1 = mayor(lista1)
lista2 = mayor(lista2)

print("El mayor es: ",lista1.mayor())
print("El mayor es: ",lista2.mayor())