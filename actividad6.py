#Declarar dos listas vaciás  una de nombres y otra de edades, ingresar el nombre de 5 personas junto con sus edades,
#se hace con  apen, se piden los nombre de los mayores de edad

nombre = []
edad = []

for x in range(5):
    nom = input("Ingrese su nombre: ")
    nombre.append(nom)
    ed = int(input("Ingrese su edad: "))
    edad.append(ed)

print("Nombre de las personas mayores de edad:")
for x in range(5):
    if edad[x]>=18:
        print(nombre[x])