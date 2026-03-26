# Se declara los datos de un alumno en un diccionario el nombrer, el curso y suss diferentes notas, se pide visulizar el nombre y la nota media

alumnos = [
    {"nombre": "Juan", "curso": "2Asir", "nota": [6, 9, 4]},
    {"nombre": "Jose", "curso": "2Asir", "nota": [4, 9, 5]}
]

def Proceso(alumnos):
    Mmedia = 0
    Mcurso = ""
    Malumno = ""

    for alumno in alumnos:
        media = sum(alumno["nota"]) / len(alumno["nota"])
        if media > Mmedia:
            Mmedia = media
            Malumno = alumno["nota"]
            Mcurso = alumno["curso"]


    return Malumno, Mmedia, Mcurso

def Visualizar(dato):
    print("Alumno con mayor media:", dato[0])
    print("Curso: ", dato[2])
    print("Media:", dato[1])

resul = Proceso(alumnos)
Visualizar(resul)

