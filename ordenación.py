# Definición de la matriz 3x3
matriz = [
    [9, 3, 5],
    [2, 8, 6],
    [7, 1, 4]
]

def bubble_sort(fila):
    # Implementación del algoritmo Bubble Sort
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                # Intercambio
                fila[j], fila[j+1] = fila[j+1], fila[j]

def ordenar_fila(matriz, fila_index):
    # Ordena la fila especificada en la matriz
    if 0 <= fila_index < len(matriz):
        bubble_sort(matriz[fila_index])
    else:
        print("Índice de fila fuera de rango.")

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

# Llamada a la función para ordenar la fila
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
