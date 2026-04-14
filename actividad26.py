# Dado una frase visualizar las diferentespalabras que contiene una en cada linea, frase = "Hoy es martes 14 de Abril"

diccio={}
frase = "casa:house,es:is,la:the,azul:blue"

tabla_pareja = frase.split(",")
for pareja in tabla_pareja:
    clave, valor = pareja.split(":")
    diccio[clave]=valor
print(diccio)

frase2 = "la casa es azul"
for palabra in frase2.split():
    if palabra in diccio:
        print(diccio[palabra], end=" ")
    else:
        print(palabra, end=" ")