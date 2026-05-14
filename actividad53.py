# Declarar 3 listas, visualizar un superlista que contenga las 3 listas

class SuperLista:
    def __init__(self, lista1, lista2, lista3):
        self.lista1 = lista1
        self.lista2 = lista2
        self.lista3 = lista3

    def superlista(self):
        super_lista = []
        super_lista.append(self.lista1)
        super_lista.append(self.lista2)
        super_lista.append(self.lista3)
        return super_lista
    
lista1 = [3,8,0,7,9,5,1]
lista2 = [9,3,4,55,2,8]
lista3 = [1,2,3,4,5]

super_lista = SuperLista(lista1, lista2, lista3)

print("Superlista: ", super_lista.superlista())