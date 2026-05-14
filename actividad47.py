class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        print(f"Alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

# Pedir datos al usuario
nombre1 = input("Introduce el nombre del alumno: ")
nota1 = float(input("Introduce la nota del alumno: "))
nombre2 = input("Introduce el nombre del alumno: ")
nota2 = float(input("Introduce la nota del alumno: "))

# Crear objeto
alumno1 = Alumno(nombre1, nota1)
alumno2 = Alumno(nombre2, nota2)

# Mostrar información
alumno1.mostrar_datos()
alumno2.mostrar_datos()