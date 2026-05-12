class Alumnos:
    profe="Rafael"
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Nota: {self.nota}, Profe: {self.profe}"
    
    @staticmethod
    def esta_aprobado(nom, n):
        if n >= 5:
            print("Aprobado " + nom)
        else:
            print("Suspenso " + nom)

alumno1 = Alumnos("Pedro", 7)
alumno2 = Alumnos("Rosa", 9)
print(alumno1)
print(alumno2)
Alumnos.esta_aprobado(alumno1.nombre, alumno1.nota)