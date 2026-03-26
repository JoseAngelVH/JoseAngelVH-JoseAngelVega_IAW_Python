# Lista formada por un nombre y las notas de ese alumno, crear un diccionario, donde la clave sea el nombre y el valor la nota

alumno=["Jose", 6, 7, 3]

def diccionario(lista):
    diccio = {}
    nombre = lista[0]
    notas = lista[1:]
    diccio [nombre] = notas
    return diccio

resultado = diccionario(alumno)
print(resultado)

#def Proceso(lista):
#    diccio={}
#    tab=[]
#    nombre = lista[0]
#    for x in range (2, len(lista)):
#        tab.append(lista[x])
#    
#    diccio[nombre]=tab
#    return diccio
#
#def Visualizar (dato)
#    print (dato)
#
#    resul = Proceso(lista)
