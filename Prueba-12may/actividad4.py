# Se declara una lista con varios diccionarios, representados en la siguiente tabla:
# A) Dado un nº de cuenta, visualizar si se encuentra o no en la lista.
# B) Visualizar la media de saldos de todos los clientes.
# C) Visalizar los nombresy número de cuenta cuyo saldo sea mayor de 30000 euros.
# Con funciones

lista = [
    {"Nº cuenta":2034056, "Nombre":"Antonio Gonzalez", "Saldo":1000},
    {"Nº cuenta":3465748, "Nombre":"Maria Torres", "Saldo":38000},
    {"Nº cuenta":4768584, "Nombre":"Javier Vaquero", "Saldo":25000},
    {"Nº cuenta":4876756, "Nombre":"Laura Moreno", "Saldo":18000},
]

def buscar_cuenta(lista):
    cuenta = int(input("Ingrese el número de cuenta a buscar: "))
    for cliente in lista:
        if cliente["Nº cuenta"] == cuenta:
            print("La cuenta se encuentra en la lista.")
            return
    print("La cuenta no se encuentra en la lista.")

def media_saldos(lista):
    conta = 0
    suma = 0
    for x in lista:
        suma += x["Saldo"]
        conta += 1
    media = suma / conta
    print("La media de saldos de todos los clientes es:", media)

def clientes_saldo_mayor(lista):
    print("Clientes con saldo mayor a 30000 euros:")
    for x in lista:
        if x["Saldo"] > 30000:
            print(f"Nombre: {x['Nombre']}, Nº cuenta: {x['Nº cuenta']}")

buscar_cuenta(lista)
media_saldos(lista)
clientes_saldo_mayor(lista)

