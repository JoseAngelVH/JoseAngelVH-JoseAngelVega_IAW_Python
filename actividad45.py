class Persona:

    def __init__(self, nombre):
        self.nombre = nombre


class Alumno(Persona):

    def __init__(self, nombre, nota):
        super().__init__(nombre)
        self.nota = nota

    def mostrar_datos(self):
        print("Alumno:", self.nombre, "- Nota:", self.nota)


class Profesor(Persona):

    def __init__(self, nombre, asignatura):
        super().__init__(nombre)
        self.asignatura = asignatura

    def mostrar_datos(self):
        print("Profesor:", self.nombre, "- Asignatura:", self.asignatura)


# -------------------------
# BLOQUE PRINCIPAL
# -------------------------

# Lista de 5 alumnos
alumnos = [
    Alumno("Pepe", 5),
    Alumno("Ana", 8),
    Alumno("Luis", 7),
    Alumno("Marta", 9),
    Alumno("Carlos", 6)
]

# Lista de 5 profesores
profesores = [
    Profesor("Carla", "Matemáticas"),
    Profesor("Juan", "Historia"),
    Profesor("Laura", "Física"),
    Profesor("Pedro", "Lengua"),
    Profesor("Sonia", "Inglés")
]

# Mostrar alumnos
print("=== ALUMNOS ===")
for alumno in alumnos:
    alumno.mostrar_datos()

# Mostrar profesores
print("\n=== PROFESORES ===")
for profesor in profesores:
    profesor.mostrar_datos()