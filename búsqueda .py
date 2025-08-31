# Definición de la matriz 3x3
dato = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def buscar_valor(dato, valor):
    for i in range(len(dato)):
        for j in range(len(dato[i])):
            if dato[i][j] == valor:
                return i, j # Retorna la posición (fila, columna)
    return None  # Retorna None si no se encuentra el valor

# Valor a buscar
valor_a_buscar = 9

# Llamada a la función de búsqueda
resultado = buscar_valor(dato, valor_a_buscar)

# Mensaje de resultado
if resultado:
    print(f"El valor {valor_a_buscar} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
