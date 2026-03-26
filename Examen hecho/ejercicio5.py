

lista1=["Jose","pepe","juan"]
lista2=["informatica","lengua","geografia"]
lista3=[]


numero = [
    {4,5,6,9},
    {8,2,9,4}
]

def proceso(numero):
    sw = False
    for x in numero:
        if x % 2 == 0:
            sw = True
    return sw

def visualizar(dato):
    print(dato)

result = proceso(numero)
visualizar (result)