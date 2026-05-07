# Delcarar un clase con su nombre y su nota. Visualizar el nombre y la nota

class Persona:
    def __init__ (self,nom,nota):
        self.nombre=nom
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

# bloque principal

persona1=Persona("Pepe",5)
persona1.imprimir()

persona2=Persona("Carla",3)
persona2.imprimir()