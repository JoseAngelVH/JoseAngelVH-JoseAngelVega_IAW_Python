#dada unna super-lista (lista de listas), por cada lista, anular todos los valores impares que se repitan. Visualizar la super-lista modificada. Tiene que ser con funciones

def anular_impares_repetidos(super_lista):
	for sublista in super_lista:
		impares_repetidos = set()
		for num in sublista:
			if num % 2 != 0 and sublista.count(num) > 1:
				impares_repetidos.add(num)
		for num in impares_repetidos:
			while num in sublista:
				sublista[sublista.index(num)] = 0
	return super_lista

super_lista = [
	[1, 2, 3, 4, 5, 3],
	[6, 7, 8, 9, 7],
	[10, 11, 12, 13, 14, 11]
]	
super_lista_modificada = anular_impares_repetidos(super_lista)
print(super_lista_modificada)


