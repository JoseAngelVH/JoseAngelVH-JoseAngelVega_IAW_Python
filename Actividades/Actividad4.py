# Se declara un diccionario, concretamente, de los productos vendidos en una tienda
# "codigo" => 11380, "cantidad_vendida" => 5, "precio" => 20
# "codigo" => 13700, "cantidad_vendida" => 4, "precio" => 12
# A) Visualizar el importe de cada venta (cantidad_vendida x precio).
# B) Visualzar los codigos de aquellos articulos cuyo importe de la venta sea superior a la media de todos los artículos.
# C) Guardar en una lista los códigos de los articulos cuyo importe de la venta sea superior a 500 euros. Visualizar la lista.

articulos = [
    {"codigo": 11380, "cantidad_vendida": 5, "precio": 20},
    {"codigo": 13700, "cantidad_vendida": 4, "precio": 12}
]

def calcular_importe(articulos):
    for articulo in articulos:
        importe = articulo["cantidad_vendida"] * articulo["precio"]
        print(f"Importe de la venta del artículo {articulo['codigo']}: {importe} euros")

def codigos_superiores_media(articulos):
    importes = [articulo["cantidad_vendida"] * articulo["precio"] for articulo in articulos]
    media_importes = sum(importes) / len(importes)
    print(f"Media de los importes: {media_importes} euros")
    codigos_superiores = [articulo["codigo"] for articulo in articulos if (articulo["cantidad_vendida"] * articulo["precio"]) > media_importes]
    print("Códigos de artículos con importe superior a la media:", codigos_superiores)

def codigos_superiores_500(articulos):
    codigos_superiores_500 = [articulo["codigo"] for articulo in articulos if (articulo["cantidad_vendida"] * articulo["precio"]) > 500]
    print("Códigos de artículos con importe superior a 500 euros:", codigos_superiores_500)

calcular_importe(articulos)
codigos_superiores_media(articulos)
codigos_superiores_500(articulos)
