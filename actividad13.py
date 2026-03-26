class Persona:

    def inicializar(self,nom):
        self.nombre=nom

    def metedinero(self,meterdinero):
        self.dinero=meterdinero

    def imprimir(self):
        print("Nombre",self.nombre)
        print("Mete dinero:",self.dinero)

persona1=Persona()
persona1.inicializar("Pedro")
persona1.metedinero("No")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla")
persona2.metedinero("Si")
persona2.imprimir()