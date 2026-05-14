class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        print(f"Alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

# Pedir datos al usuario
nombre = input("Introduce el nombre del alumno: ")
nota = float(input("Introduce la nota del alumno: "))

# Crear objeto
alumno1 = Alumno(nombre, nota)

# Mostrar información
alumno1.mostrar_datos()
alumno1.comprobar_aprobado()