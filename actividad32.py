# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene
# y los kilometros que conducen cada dia de la semana
# Para guardar esta información se van a utilizar dos arreglos:
# nombre: listaa para guardar los nombres de los conductores
# kilometros: tabla para guardar los kilometros que realizancada dia de la semana
# Se quere generar una nueva lista ("total_kms") con los kilometros totales que realza cada conductor
# AL finalizar se muestra la lista con los nombres de conductores y los kilometros que ha realizado

nombre = []
kilometro = []

def proceso(nombre,kilometro):
    sw = 0
    while sw == 0:
        nombre_con = input("Escribe su nnombre: ")
        nombre.append(nombre_con)
        km_con = []
        for i in range(7):
            km = float(input(f"Escribe los kilometros que ha conducido el dia {i+1}: "))
            km_con.append(km)
        kilometro.append(km_con)
        sw = int(input("¿Quieres añadir otro trabajador? (0 para sí, 1 para no): "))

def total_kms(kilometro):
    total_kms = []
    for km_con in kilometro:
        total_kms.append(sum(km_con))
    return total_kms

def visualizar(nombre, total_kms):
    for i in range(len(nombre)):
        print(f"Conductor: {nombre[i]}, total de kilómetros: {total_kms[i]}")

proceso(nombre, kilometro)
total_kms_resultado = total_kms(kilometro)
visualizar(nombre, total_kms_resultado)