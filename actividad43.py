# Se pide los nombre de 5 alumnos por teclado cada uno con su nota correspondiente. 
# Los nombres se guarda en un array y las notas en otro array. Se pide visualizar el nombre del alumno con mayor nota

class Alumnos:
    def __init__(self):
        self.alumnos = []
        self.notas = []

    def cargar_datos(self):
        for i in range(5):
            nombre = input("Ingrese su nombre:")
            nota = input("Ingrese su nota:")

            self.alumnos.append(nombre)
            self.notas.append(nota)

    def mayor_nota(self):
        nota_max = self.notas[0]
        posicion = 0
        for i in range(1, len(self.notas)):
            if self.notas[i] > nota_max:
                nota_max = self.notas[i]
                posicion = i
        
        print("El alumno con mayor nota es: ", self.alumnos[posicion], "con una nota de: ", nota_max)

    def imprimir(self):
        for i in range(len(self.alumnos)):
            print("Nombre: ",self.alumnos[i])
            print("Nota: ",self.notas[i])

# bloque principal

alumnos1=Alumnos()
alumnos1.cargar_datos()
alumnos1.imprimir()
alumnos1.mayor_nota()
