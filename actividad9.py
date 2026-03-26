# Escribir un programa que almacene el diccionario con los créditos de las asignturas de un curso {"matematicas": 6, "Fisica": 4, "Química": 5}
# y después muestre por pantalla los créditos de cada asignatura en el formato "<asignatura> tiene <créditos> créditos", donde "<asignatura>
# es cada una de las asignaturas del curso, y "<créditos>" son sus créditos.
# Al final debe ostrar también el número total de créditos del curso

curso={
    'matematicas': 6, 
    'fisica': 4, 
    'quimica': 5
}

def Proceso(curso):
    total_creditos = 0
    for asignatura, creditos in curso.items():
        print(asignatura, 'tiene', creditos, 'créditos')
        total_creditos += creditos

    return total_creditos
def Visualizar(dato):
    print('Número total de créditoss del curdo_ ', total_creditos)

Proceso(curso)