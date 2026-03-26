# Se declara un diccionario con los contagios que ha habido en las distintas localidades en la última semana de lunes a viernes:
# lunes "Chiclaana" => 130, "Conil" => 220, "San Fernando" => 300
# martes "Chiclaana" => 100, "Conil" => 200, "San Fernando" => 280
# .....................................
# a) Visualizar el número total de contagios, por localidad, que ha habido el martes (segunda fila)
# b) Visualizar la suma de los contagios que ha habido en Chiclana.
# c) Visulizar en que dia de la semana ha habido mas contagios.

contagios = {
    "lunes": {"Chiclana": 130, "Conil": 220, "San Fernando": 300},
    "martes": {"Chiclana": 100, "Conil": 200, "San Fernando": 280},
    "miercoles": {"Chiclana": 90, "Conil": 180, "San Fernando": 330},
    "jueves": {"Chiclana": 70, "Conil": 210, "San Fernando": 290},
    "viernes": {"Chiclana": 85, "Conil": 190, "San Fernando": 310},
}

def contagio_localidad(contagios):
    return contagios["martes"]
print("martes: ",contagio_localidad(contagios))

def contagio_chiclana(contagios):
    suma = 0
    for clave, valor in contagios.items():
        suma += valor["Chiclana"]
    return suma
print(contagio_chiclana(contagios))

