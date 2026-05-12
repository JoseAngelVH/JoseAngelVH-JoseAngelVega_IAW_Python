# A partir del teclado, almacenar el nombre, cruso y año de naciemiento de un solo alumno en un diccionario donde el nombre, curso y año de nmacimiento sean las claves o índices.
# Visualizar el diccionario

alumno = {}

def almacenar_datos(alumno):
    alumno['Nombre'] = input("Introduce el nombre del alumno: ")
    alumno['Curso'] = input("Introduce el curso del alumno: ")
    alumno['Año_nacimiento'] = int(input("Introduce el año de nacimiento del alumno: "))
    return alumno

def visualizar_datos(alumno):
    print("Diccionario completo:", alumno)

alumno = almacenar_datos(alumno)
visualizar_datos(alumno)