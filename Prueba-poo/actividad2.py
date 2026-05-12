class Numero:

    mensaje = "El numero es: "

    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"{Numero.mensaje}{self.valor}")

    # Sobrecarga del operador +
    def __add__(self, otro):
        return Numero(self.valor + otro.valor)


# Crear objetos
mi_numero1 = Numero(42)
mi_numero2 = Numero(53)

# Sumar objetos
mi_numero3 = mi_numero1 + mi_numero2

# Mostrar resultados
mi_numero1.mostrar()
mi_numero2.mostrar()
mi_numero3.mostrar()