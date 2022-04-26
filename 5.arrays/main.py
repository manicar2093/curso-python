# Arrays

nombres = [
    "Rodrigo",
    "Mariana",
    "Ara",
    "Dann",
    "Manuel",
]

print(nombres)

# Se comienza a contar desde 0
# Asi se accede a los datos de un array

print(nombres[0])
print(nombres[2])
print(nombres[4])

# len() para conocer la longitud de un array
print(len(nombres))


# Se puede asignar valores a los indices de un arreglo

nombres[0] = "Ernesto"
nombres[4] = "Fulanito"

print(nombres)

# datos = [
#    "Dennis", # Nombre
#    25, # Edad
#    "1.5", # Altura
#    True, # Es programadora
# ]
# print(datos)
# print("Mi nombre es " + datos[0] + " y mido " + datos[2])

# Agregar mas datos al array

nombres.append("Vega")
nombres.append("Robles")
nombres.append("Carpenter")
print(nombres)

# Da error: IndexError: list assignment index out of range
# nombres[10] = "Dato"

print(nombres[len(nombres) - 1])

# Los strings "tambien son arreglos"

integrante = "Jose Perez Gonzalez"
print(integrante[5])
