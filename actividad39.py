class CuentaCliente:
    def __init__(self, nombre, saldo=0):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito realizado. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro realizado. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")

    def mostrar_saldo(self):
        print(f"Cliente: {self.nombre} | Saldo actual: {self.saldo}")


# Ejemplo de uso
cuenta1 = CuentaCliente("Juan Pérez", 100)

cuenta1.mostrar_saldo()
cuenta1.depositar(50)
cuenta1.retirar(30)
cuenta1.retirar(200)
cuenta1.mostrar_saldo()