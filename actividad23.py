# Declarar una super-lista con la siguiente información:
# fila0 4 7 9 45
# fila1 1 5 6 3
# fila2 20 30 10 3
# fila3 7 15 3 477
# fila4 5 40 30 10
# En la fila 0, si o no existe un valor que sea múltiplo de el de la izquierda y derecha.

superlista=[
    ["fila0", 4, 7, 9, 45],
    ["fila1", 1, 5, 5, 3],
    ["fila2", 20, 5, 5, 3],
    ["fila3", 7, 5, 5, 477],
    ["fila4", 5, 40, 30, 10]
]

def Proceso2(superlista,fila):
    resul=0
    for col, valor in enumerate(superlista[fila][1:], start=1):
        todos_multiplos = "si"
        izq = der = "si"
        if col == 1: izq="no"
        if col == len(superlista[fila])-1: der="no"
        
        if izq == "si":
            if valor % superlista[fila][col-1] != 0:
                todos_multiplos = "no"
       
        if der == "si" and todos_multiplos == "si":
            if valor % superlista[fila][col+1] != 0:
                todos_multiplos = "no"
      
        if todos_multiplos == "si":
            resul = 1
            
    return resul
    


    
def Proceso(superlista):
    print (superlista[0][0])
    if Proceso2(superlista, 0) == 1:
        print ("si")
    else:
        print ("no")
                
               
Proceso(superlista)