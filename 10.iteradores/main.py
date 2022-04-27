# Iteradores

# Recordando los array
# nombres = ["Rodrigo", "Ara", "Dann", "Manuel"]
# nombres[0]
# nombres[1]
# nombres[2]
# nombres[3]
# nombres[4] # Error

# For. Nos sirver para recorrer un arreglo

# for nombre in nombres:
#     print("Nombre encontrado:", nombre)

# transacciones = [
#     {
#         'monto': 20.0,
#         'destino': "tiendita",
#     },
#     {
#         'monto': 260.0,
#         'destino': "Coppel",
#     },
#     {
#         'monto': 80.0,
#         'destino': "Burguer",
#     },
# ]

# for trx in transacciones:
#     print(trx)

# Contamos con las palabras reservadas "continue" y "break"

nombres = ["Rodrigo", "Ara", "Dann", "Manuel"]

# break terminará la iteración sin importar que el arreglo contenga mas información para recorrer

# for nombre in nombres:
#     if nombre == "Ara":
#         print("Te encontramos,", nombre)
#         print("Ya no tenemos que seguir buscando. ¡Vamos a usar break! :3")
#         break

# continue indicará que la iteración debe ir al siguiente elemento

# for nombre in nombres:
#     if nombre == "Rodrigo":
#         print("Te encontramos,", nombre)
#         print("Quizá haya otro Rodrigo. ¡Vamos a continuar buscando!")
#         print()
#         continue
#     print(nombre, "¿Viste a algún Rodrigo por aquí? :P")


# transacciones = [
#     {
#         'monto': 20.0,
#         'destino': "tiendita",
#         'status': "PENDIENTE",
#     },
#     {
#         'monto': 260.0,
#         'destino': "Coppel",
#         'status': "PENDIENTE",
#     },
#     {
#         'monto': 260.0,
#         'destino': "Coppel",
#         'status': "PENDIENTE",
#     },
#     {
#         'monto': 80.0,
#         'destino': "Burguer",
#         'status': "IN_PROCESS",
#     },
# ]

# for tx in transacciones:
#     if tx['status'] == 'PENDIENTE':
#         print("ENVIANDO TRANSACCION A CORE BANCARIO")
#         continue
#     elif tx['status'] == "FAILED":
#         print("NO SE PUEDE CONTINUAR ENVIANDO TRANSACCIONES")
#         break
#     else:
#         print("TRANSACCION EN PROCESO")
    


# While. "Mientras". Repite lo que se encuentre en su bloque de codigo hasta que la condición ya no sea True

# contador = 0
# while contador < 10:
#     print("cuenta va en:", contador)
#     contador = contador + 1

# contador = 0
# while contador < len(nombres):
#     print(nombres[contador])
#     contador += 1
