import pandas as pd



df = pd.DataFrame(data)

df.to_excel('grabar.xlsx', index=False, sheet_name="Hoja1")