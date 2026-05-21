# Crea un programa que almacene las notas de varios alumnos usando un diccionario deonde
# * La clave será el nombre del alumno
# * El valor sera una lista de listas con sus asignaturas y notas
# 1. Mostrar todos los alumnos y sus notas
# 2. Mostrar la media de notas de un alumno concreto
# 3. Mostrar que alumno tiene la nota mas alta en una asignatura determinada
# 4. Añadir una nueva asignatura y nota a un alumno
# 5. Mostrar todos los alumnos aprobados en una asignatura concreta

alumnos = {
    "Ana":[["Python",8],["SQL",7],["Redes",9]],
    "Luis":[["Python",5],["SQL",6]],
    "Marta":[["Redes",10],["Python",9]]
}

def mostrar_alumnos(alumnos):
    for alumno, notas in alumnos.items():
        print(f"Alumno: {alumno}")
        for asignatura, nota in notas:
            print(f"  Asignatura: {asignatura}, Nota: {nota}")

mostrar_alumnos(alumnos)


def media_alumno(alumnos, nombre):
    if nombre in alumnos:
        notas = [nota for asignatura, nota in alumnos[nombre]]
        media = sum(notas) / len(notas)
        print(f"Media de {nombre}: {media:.2f}")
    else:
        print(f"Alumno {nombre} no encontrado.")

media_alumno(alumnos,"Ana")


def alumno_nota_alta(alumnos, asignatura):
    alumno_con_nota_alta = None
    nota_alta = -1
    for alumno, notas in alumnos.items():
        for asignatura_nota in notas:
            if asignatura_nota[0] == asignatura and asignatura_nota[1] > nota_alta:
                nota_alta = asignatura_nota[1]
                alumno_con_nota_alta = alumno
    if alumno_con_nota_alta:
        print(f"Alumno con la nota más alta en {asignatura}: {alumno_con_nota_alta} con una nota de {nota_alta}")
    else:
        print(f"No se encontró la asignatura {asignatura}.")

alumno_nota_alta(alumnos,"Python")


def añadir_asignatura(alumnos, nombre, asignatura, nota):
    if nombre in alumnos:
        alumnos[nombre].append([asignatura, nota])
        print(f"Asignatura {asignatura} con nota {nota} añadida a {nombre}.")
    else:
        print(f"Alumno {nombre} no encontrado.")

añadir_asignatura(alumnos, "Luis", "Redes", 7)


def alumnos_aprobados(alumnos, asignatura):
    aprobados = []
    for alumno, notas in alumnos.items():
        for asignatura_nota in notas:
            if asignatura_nota[0] == asignatura and asignatura_nota[1] >= 5:
                aprobados.append(alumno)
                break
    print(f"Alumnos aprobados en {asignatura}: {', '.join(aprobados)}")

alumnos_aprobados(alumnos, "Redes")