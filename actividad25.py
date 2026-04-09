# Un programa para traaducir de lenguaje catellano a otro, para ello se le pide al usuario parejas de valores separadas por comas.
# Cada pareja contiene la palabra en castellano: ingles y la pajera de valores separadas por comas
# Se le pide que introduzca una frase en catellano y el programa debe de traducirla.

def crear_diccionario():
    diccionario = {}
    while True:
        entrada = input("Introduce una pareja de palabras (castellano:ingles) o 'salir' para terminar: ")
        if entrada.lower() == 'salir':
            break
        try:
            castellano, ingles = entrada.split(':')
            diccionario[castellano.strip()] = ingles.strip()
        except ValueError:
            print("Entrada no válida. Por favor, introduce la pareja de palabras en el formato correcto.")
    return diccionario

def traducir_frase(diccionario):
    frase = input("Introduce una frase en castellano para traducir: ")
    palabras = frase.split()
    traduccion = []
    for palabra in palabras:
        traduccion.append(diccionario.get(palabra, palabra))
    return ' '.join(traduccion)

def main():
    diccionario = crear_diccionario()
    traduccion = traducir_frase(diccionario)
    print("Frase traducida:", traduccion)
if __name__ == "__main__":    main()

