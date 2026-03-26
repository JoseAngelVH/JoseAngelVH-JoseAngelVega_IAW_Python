# Guardar los nombres de los alumnos de una clase y las notas que han obtenido.Cada alumno puede tener distinta cantidad de notas. Gurda la información en un diccionario cuyas claves serán los nombres de los  alumnos y los valores serán listas con las notas de cada alumno. El programa pedirá el numero de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se  introduce el nombre de un alumno que ya existe el programa nos dará error.

def obtener_notas_alumnos():
    alumnos = {}
    num_alumnos = int(input("Introduce el número de alumnos: "))
    
    for _ in range(num_alumnos):
        nombre = input("Introduce el nombre del alumno: ")
        if nombre in alumnos:
            print("Error: El alumno ya existe.")
            continue
        
        notas = []
        while True:
            nota = float(input("Introduce una nota (negativa para terminar): "))
            if nota < 0:
                break
            notas.append(nota)
        
        alumnos[nombre] = notas
    
    return alumnos

def calcular_notas_media(alumnos):
    notas_media = {}
    for nombre, notas in alumnos.items():
        if notas:
            notas_media[nombre] = sum(notas) / len(notas)
        else:
            notas_media[nombre] = 0
    return notas_media

alumnos = obtener_notas_alumnos()
notas_media = calcular_notas_media(alumnos)
print("Alumnos y sus notas medias:")
for nombre, media in notas_media.items():
    print(f"{nombre}: {media:.2f}")
