class Persona:

    def __init__(self,nombre):
        self.nombre = nombre

class Alumno(Persona):

    def __init__(self, nombre, nota):
        super().__init__(nombre)
        self.nota = nota

    def mostrar_datos(self):
        print("Alumno: ", self.nombre, " nota: ",self.nota)

class Profesor(Persona):

    def __init__(self, nombre, asignatura):
        super().__init__(nombre)
        self.asignatura = asignatura

    def mostrar_datos(self):
        print("Profesor: ", self.nombre, " asignatura: ", self.asignatura)

# bloque principal

alumno1 = Alumno("Pepe", 5)
alumno1.mostrar_datos()

profesor1 = Profesor("Carla", "Matematicas")
profesor1.mostrar_datos()
