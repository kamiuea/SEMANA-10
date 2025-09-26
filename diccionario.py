# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "kenia Medranda",
    "edad": 31,
    "ciudad": "manta",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
print("Ciudad antes de modificar:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "portoviejo"  # Modificando la ciudad
print("Ciudad después de modificar:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor para "telefono"
if "telefono" not in informacion_personal:  # Verificar si la clave "telefono" existe
    informacion_personal["telefono"] = "0988636680"  # Agregando un número de teléfono ficticio

# Eliminar la clave "edad"
if "edad" in informacion_personal:  # Verificar si la clave "edad" existe antes de eliminar
    del informacion_personal["edad"]  # Eliminando la clave "edad"

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
