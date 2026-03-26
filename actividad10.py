# Declarar 2 litas con valores numericos ambas del mismo tamaño y si no es del mismo tamaño tiene que dar error,
# en caso de mismo tamaño obetener otra lista con aquellos valores que esten en ambas listas, que sean iguales y que esten en la misma posición

lista1=[1,2,3,4,5]
lista2=[6,7,8,9,10]

def Proceso(lista1, lista2):
    listaiguales=[]
    if len(lista1) != len(lista2):
        print("Error no son del mismo tamaño")
        return listaiguales

    else:
        for i in range(len(lista1)):
            if lista1[i] == lista2[i]:
                listaiguales.append(lista1[i])
    return listaiguales

def Visualizar(listaiguales):
    for x in listaiguales:
        print(x)

tab_resul = Proceso(lista1, lista2)
Visualizar (tab_resul)