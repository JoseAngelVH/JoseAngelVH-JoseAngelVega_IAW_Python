class Alumnos:
    profe="Rafael"
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Nota: {self.nota}, Profe: {self.profe}"
    
    @classmethod
    def cambio_profe(cls, profe):
        cls.profe = profe

alumno1 = Alumnos("Pedro", 7)
alumno2 = Alumnos("Rosa", 9)
print(alumno1)
print(alumno2)