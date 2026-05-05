class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f"Nota añadida. Notas actuales: {self.notas}")
        else:
            print("La nota debe estar entre 0 y 10.")

    def eliminar_nota(self, nota):
        if nota in self.notas:
            self.notas.remove(nota)
            print(f"Nota eliminada. Notas actuales: {self.notas}")
        else:
            print("Esa nota no existe.")

    def mostrar_notas(self):
        print(f"Estudiante: {self.nombre} | Notas: {self.notas}")

    def calcular_promedio(self):
        if len(self.notas) == 0:
            print("No hay notas para calcular promedio.")
        else:
            promedio = sum(self.notas) / len(self.notas)
            print(f"Promedio: {promedio:.2f}")


# Ejemplo de uso
est1 = Estudiante("Ana López")

est1.mostrar_notas()
est1.agregar_nota(8)
est1.agregar_nota(9)
est1.agregar_nota(7)
est1.eliminar_nota(9)
est1.calcular_promedio()