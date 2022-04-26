# dict

# Recordemos los array
nombres = ["Marianna", "Ara", "Rodrigo", "Manuel"]
# print(nombres[0])

# key: value
empleado = {
    # key:    value
    "nombre": "Marianna",
    "horario": 8,
    "vacaciones": False,
}

# print(empleado)
# print(empleado["vacaciones"])
# print(empleado["nombre"])

# Caracteristicas de los diccionarios (dict)

# 1. No permiter keys duplicados

empleado = {
    # key:    value
    "nombre": "Marianna",
    "horario": 8,
    "vacaciones": False,
    "nombre": "David",
}

# print(empleado)

# 2. Podemos saber la cantidad de keys que hay dentro un diccionario

# print(len(empleado))

# 3. El key puede ser de cualquier tipo de dato

empleado[45] = "temperatura"
# print(empleado)
# print(empleado[45])
# empleado[23.1] = True
# print(empleado)

# La forma de ingresar a los valores que se guardan en los key es:
# usando los corchetes y sabiendo el key necesario

# print(empleado["nombre"])

# Cómo agregamos una nueva key

# empleado["nueva_key"] = "nuevo_valor"
# print(empleado)

# Cambiar el valor de una key
# Si existe cambia el valor. Si no existe
# agregará el key con el valor

empleado["nombre"] = "Ara"
# print(empleado)

tx1 = {
    "usuario": "Jose",
    "clave_rastreo": 456789,
    "fecha": "2022-01-01",
    "monto": 1523.23,
}
print(tx1)

nuevo_monto = tx1["monto"] + 5
nuevo_usuario = tx1["usuario"] + "_aplicado"

tx1["usuario"] = nuevo_usuario
tx1["monto"] = nuevo_monto

print(tx1)
