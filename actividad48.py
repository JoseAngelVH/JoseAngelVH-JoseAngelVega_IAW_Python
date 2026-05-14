class Alumno:

    profesor = "Juan"

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"Nombre: {self.nombre}, Nota: {self.nota}, Profesor: {self.profesor}"

# Crear objeto
alumno1 = Alumno("jose", 8)
alumno2 = Alumno("Rosa", 9)

# Mostrar información
print(alumno1)
print(alumno2)