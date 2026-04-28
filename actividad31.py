import matplotlib.pyplot as plt

categorias = ["Alquiler", "Comida", "Transporte", "Ocio", "Otros"]

gastos = [700, 250, 100, 150, 80]

plt.pie(gastos, labels=categorias, autopct='%1.1f%%')
plt.title("Distribución de gastos mensuales")

plt.show()