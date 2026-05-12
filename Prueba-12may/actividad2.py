# Se considera un diccionario con las notas de un alumno en distintas asignaturas.
# Se pide, visualizar el nombre de la asignatura en la que ha obtenido menor nota.

notas = {
    'Matematicas': 6,
    'Lengua': 5,
    'Inglés': 8,
    'Informatica': 7
}

def menor_nota(notas):
    conta = 0
    for asignatura, nota in notas.items():
        if conta == 0:
            menor_nota = nota
            asignatura_menor = asignatura
        else:
            if nota < menor_nota:
                menor_nota = nota
                asignatura_menor = asignatura
        conta += 1
    return asignatura_menor

asignatura_menor = menor_nota(notas)
print("La asignatura con menor nota es:", asignatura_menor)
