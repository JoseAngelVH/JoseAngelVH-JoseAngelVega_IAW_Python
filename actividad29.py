# Coger un archivo xslx llamado ventas2.xslx y añadir una columna llamada "Total" que tiene que ser vetas * precios y que se añda al excel.

import pandas as pd
df = pd.read_excel('ventas2.xlsx')
df['Total'] = df['Ventas'] * df['Precios']
df["Fecha"] = df["Fecha"].dt.strftime('%d/%m/%Y')  
df.to_excel('ventas2.xlsx', index=False)
