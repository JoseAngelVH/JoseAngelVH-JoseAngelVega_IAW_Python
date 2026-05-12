class Numero:

    mensaje = "El numero es: "

    def __init__(self, valor):
        self.valor = valor

    # Sobrecarga del operador +
    def __add__(self, otro):
        return Numero(self.valor + otro.valor)

    # Representación en texto del objeto
    def __str__(self):
        return f"{Numero.mensaje}{self.valor}"


# Crear objetos
mi_numero1 = Numero(42)
mi_numero2 = Numero(53)

# Sumar objetos
mi_numero3 = mi_numero1 + mi_numero2

# Mostrar resultados
print(mi_numero1)
print(mi_numero2)
print(mi_numero3)