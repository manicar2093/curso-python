# Recordemos los booleanos
# True
# False

# edad = int(input('¿Cuál es tu edad? '))

# es_mayor_de_edad = edad >= 18

# print("Respuesta:", es_mayor_de_edad)

# Operadores logicos
# < menor que
# > mayor que
# == igual
# <= menor igual que
# >= mayor igual que

# nombre = input("¿Cuál es tu nombre? ")

# es_igual_a = nombre == "Ernesto"

# print("Respuesta:", es_igual_a)

# and(y) or(o)

edad = 18
nombre = "Gabriel"

# El operador and nos dice que las dos sentencias deben ser verdaderas
# para que toda la expresión sea Verdadera
dar_informacion = edad >= 18 and nombre == "Ana"
print("dar_informacion: ", dar_informacion)

# El operador or nos dice que una sola sentencia debe ser verdadera
# para que toda la expresión sea verdadera
dar_informacion_2 = nombre == "Ana" or edad >= 18
print("dar_informacion_2: ", dar_informacion_2)

# Case sensitive.
compararar_strings = "Manuel" == "manuel" # False
