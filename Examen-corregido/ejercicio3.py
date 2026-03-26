# Un programa que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. 
# Cada alumno puede tener distinta cantidad de notas. Guardar la informaaciónen un diccionario cuya claves 
# serán los nombre de los alumnos y los valores serán listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedrirá su nombre e ira pidiendo sus notas 
# hasta que introduzaca un número negativo. Al final el programa nos mostrará la listas de alumnos y la nota media 
# obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

def obtener_notas_alumnos():
    alumnos = {}
    num_alumnos = int(input("Introduce el número de alumnos: "))
    for _ in range(num_alumnos):
        nombre = input("Introduce el nombre del alumno: ")
        if nombre in alumnos:
            print("Error: El alumno ya existe.")
            continue
        notas = []
        fin = "no"
        while fin == "no":
            nota = float(input("Introduce una nota (negativa para terminar): "))
            if nota < 0:
                fin = "si"
            else:
                notas.append(nota)
        alumnos[nombre] = notas
    return alumnos

def mostrar_resultados(alumnos):
    for nombre, notas in alumnos.items():
        if notas:
            media = sum(notas) / len(notas)
            print(f"Alumno: {nombre}, Nota media: {media:.2f}")
        else:
            print(f"Alumno: {nombre}, No hay notas disponibles.")

alumnos = obtener_notas_alumnos()
mostrar_resultados(alumnos)