import matplotlib.pyplot as plt

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

temperaturas = [22, 24, 21, 23, 25, 27, 26]

plt.plot(dias, temperaturas, marker='.')
plt.title("Temperaturas de la semana")
plt.xlabel("Días")
plt.ylabel("Temperatura (°C)")
plt.grid()

plt.show()