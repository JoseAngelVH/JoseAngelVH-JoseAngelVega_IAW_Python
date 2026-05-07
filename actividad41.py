class Persona:
    def __init__ (self,nom,nota):
        self.nombre=nom
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostar_aprobado(self):
        if self.nota >=5:
            print("Aprobado")
        else:
            print("Suspenso")


# bloque principal

persona1=Persona("Pepe",5)
persona1.imprimir()
persona1.mostar_aprobado()

persona2=Persona("Carla",3)
persona2.imprimir()
persona2.mostar_aprobado()