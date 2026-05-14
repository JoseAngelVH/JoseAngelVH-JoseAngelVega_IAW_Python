# Declarar una lista con valores numericos enteros. Visualizar el mayor.


class mayor:
    def __init__(self, lista):
        self.lista = lista

    def mayor(self):
        mayor = max(self.lista)
        return mayor

lista = [3,8,0,7,9,5,1]

lista1 = mayor(lista)

print("El mayor es: ",lista1.mayor())