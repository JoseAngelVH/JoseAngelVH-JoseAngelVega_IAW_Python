# Dada un frase reemplazar cada vocal por la siguiente, ejemplo = mesa -> mise

def reemplazar_vocales(frase):
    vocales = 'aeiouAEIOU'
    reemplazos = 'eiouaEIOUA'
    resultado = ''
    
    for char in frase:
        if char in vocales:
            indice = vocales.index(char)
            resultado += reemplazos[indice]
        else:
            resultado += char
            
    return resultado   

frase_usuario = input("Ingrese una frase: ")
frase_modificada = reemplazar_vocales(frase_usuario)
print("Frase modificada:", frase_modificada)