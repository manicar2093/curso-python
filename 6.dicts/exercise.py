horarios = {
    "Marianna": "14:00",
    "Daniel": "13:45",
    "Rodrigo": "14:30",
    "Ara": "14:00",
}

# nombre_solicitado = input("¿De quien quieres saber el horario? ")

# print("El horario para", nombre_solicitado, "es", horarios[nombre_solicitado])

nombre_solicitado = input("¿A quien quieres cambiarle el horario? ")
nuevo_horario = input("¿Cúal es el nuevo horario? ")

horarios[nombre_solicitado] = nuevo_horario

print("Los nuevos horarios son", horarios)
