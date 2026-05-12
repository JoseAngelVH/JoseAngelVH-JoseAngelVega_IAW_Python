class Numero:

    mensaje = "El numero es: "

    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"{self.mensaje}{self.valor}")

    @classmethod
    def cambio_mensaje(cls, mensaje):
        cls.mensaje = mensaje

# Crear un objeto
mi_numero1 = Numero(42)

# Usar el objeto
mi_numero1.mostrar()

Numero.cambio_mensaje("El resultado es: ")
mi_numero1.mostrar()
