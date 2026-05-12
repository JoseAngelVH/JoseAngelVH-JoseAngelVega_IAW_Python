class Numero:
    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"El número es: {self.valor}")


# Crear un objeto
mi_numero = Numero(42)

# Usar el objeto
mi_numero.mostrar()