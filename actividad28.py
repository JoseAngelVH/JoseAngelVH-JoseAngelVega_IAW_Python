# Coger un archivo xslx llamado ventas.xslx y Visualizar en la columna ventas  las ventas que sean mayores a 1200.

import pandas as pd
df = pd.read_excel('ventas.xlsx')
ventas_mayores = df[df['Ventas'] > 1200]
print(ventas_mayores) 