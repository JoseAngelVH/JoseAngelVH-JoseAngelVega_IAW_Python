# Implementar unn diccionario con las notas de un alumno en las tres evaluaciones
# A) Pasar solo las notas a una sola estructura de la lista con sublistas
# B) A partir de esta ultima estructura obtener la media de cada evaluación
# C) A partir de esta ultima estructura obtener la media de cada asignatura

notas = {
    '1ºeval': {"Matematicas": 6, "Lengua": 4, "Ingles": 8, "Informática": 7},
    '2ºeval': {"Matematicas": 5, "Lengua": 3, "Ingles": 7, "Informática": 8},
    '3ºeval': {"Matematicas": 5, "Lengua": 4, "Ingles": 7, "Informática": 9},
}

def extraer_notas(notas):
    lista_notas = []
    for evaluacion in notas.values():
        lista_notas.append(list(evaluacion.values()))
    return lista_notas

notas_lista = extraer_notas(notas)
print("Notas en lista de sublistas:", notas_lista)


def calcular_medias_evaluacion(notas_lista):
    medias = []
    for evaluacion in notas_lista:
        media = sum(evaluacion) / len(evaluacion)
        medias.append(media)
    return medias

medias_evaluacion = calcular_medias_evaluacion(notas_lista)
print("Medias de cada evaluación:", medias_evaluacion)


def calcular_medias_asignatura(notas_lista):
    medias = []
    num_asignaturas = len(notas_lista[0])
    for i in range(num_asignaturas):
        suma = sum(notas_lista[j][i] for j in range(len(notas_lista)))
        media = suma / len(notas_lista)
        medias.append(media)
    return medias

medias_asignatura = calcular_medias_asignatura(notas_lista)
print("Medias de cada asignatura:", medias_asignatura)