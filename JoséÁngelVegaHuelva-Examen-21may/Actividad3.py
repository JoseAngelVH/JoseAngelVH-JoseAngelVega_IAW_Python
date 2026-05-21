# Se declara un diccionarioc, concretamente, de los productos vendidos en una tienda
# A) Visualizar el importe de cada venta (cantidad_vendida x precio)
# B) Visualizar los codigos de aquellos artículos cuyo importe de la venta sea superior a la media de todos los articulos
# C) Guardar en una lista los codidgos de los articulos cuyo importe de la venta sea superior a 500 euros. Visualizar la lista.

articulos = [
    {"codigo": 11380,"cantidad_vendida":5,"precio":20},
    {"codigo": 13700,"cantidad_vendida":4,"precio":12}
]

def calcular_importe(articulos):
    for articulo in articulos:
        importe = articulo["cantidad_vendida"] * articulo["precio"]
        print(f"El importe de la venta del articulos {articulo['codigo']}: {importe} euros")

calcular_importe(articulos)


def codigos_superiores_media(articulos):
    importes = [articulo["cantidad_vendida"] * articulo["precio"] for articulo in articulos]
    media_importes = sum(importes) / len(importes)
    print(f"Media de los importes: {media_importes} euros")
    for articulo in articulos:
        if (articulo["cantidad_vendida"] * articulo["precio"]) > media_importes:
            codigos_superiores = articulo["codigo"]
            print("Códigos de artículos con importe superior a la media:", codigos_superiores)

codigos_superiores_media(articulos)


def codigos_superiores_500(articulos):
    codigos_superiores_500 = [articulo["codigo"] for articulo in articulos if (articulo["cantidad_vendida"] * articulo["precio"]) > 500]
    print("Códigos de artículos con importe superior a 500 euros:", codigos_superiores_500)

codigos_superiores_500(articulos)