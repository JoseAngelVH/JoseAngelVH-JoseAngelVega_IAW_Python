#Declarar un clase alumno, que contenga el nombre del alumno y su nota, ademas una funcion que permita subit esa nota y otra para bajar la nota maximo un punto.

class Alumno:
    def __init__(self, nombre, nota): 
        self.nombre = nombre 
        self.nota = nota 
        
    def subir_nota(self): 
        self.nota += 1

    def bajar_nota(self):
        self.nota -= 1 

alumno1 = Alumno("Jose", 8)

print(f"Nombre: {alumno1.nombre}, nota: {alumno1.nota}")

alumno1.subir_nota()

print(f"Nombre: {alumno1.nombre}, nota: {alumno1.nota}")

alumno1.bajar_nota()

print(f"Nombre: {alumno1.nombre}, nota: {alumno1.nota}")
