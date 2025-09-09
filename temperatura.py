# Definición de la matriz 3D: [ciudades][días de la semana][semanas]
temperaturas = [
    [  # Ciudad 1
        [30, 32, 31, 29, 28, 30, 31],  # Semana 1
        [31, 33, 30, 32, 29, 31, 30],  # Semana 2
        [28, 29, 30, 31, 30, 32, 33],  # Semana 3
        [29, 30, 31, 32, 31, 30, 29]   # Semana 4
    ],
    [  # Ciudad 2
        [25, 27, 26, 28, 27, 26, 25],  # Semana 1
        [26, 28, 27, 29, 28, 27, 26],  # Semana 2
        [27, 29, 28, 30, 29, 28, 27],  # Semana 3
        [28, 30, 29, 31, 30, 29, 28]   # Semana 4
    ],
    [  # Ciudad 3
        [20, 22, 21, 23, 22, 21, 20],  # Semana 1
        [21, 23, 22, 24, 23, 22, 21],  # Semana 2
        [22, 24, 23, 25, 24, 23, 22],  # Semana 3
        [23, 25, 24, 26, 25, 24, 23]   # Semana 4
    ]
]
# Inicializamos una lista para almacenar los promedios
promedios = []

# Iteramos sobre las ciudades
for ciudad in range(len(temperaturas)):
    promedios_ciudad = []

    # Iteramos sobre las semanas
    for semana in range(len(temperaturas[ciudad])):
        suma_temperaturas = 0

        # Iteramos sobre los días de la semana
        for dia in range(len(temperaturas[ciudad][semana])):
            suma_temperaturas += temperaturas[ciudad][semana][dia]

        # Calculamos el promedio para la semana
        promedio_semana = suma_temperaturas / len(temperaturas[ciudad][semana])
        promedios_ciudad.append(promedio_semana)

def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de varias ciudades durante un periodo de tiempo.

    :param temperaturas: list, matriz 3D donde las dimensiones son
                        [ciudades][semanas][días].
    :return: list, lista de promedios de temperatura por ciudad.
    """
    promedios_ciudades = []
    # Iteramos sobre las ciudades
    for ciudad in range(len(temperaturas)):
        suma_temperaturas = 0
        total_dias = 0

        # Iteramos sobre las semanas
        for semana in range(len(temperaturas[ciudad])):
            # Iteramos sobre los días de la semana
            for dia in range(len(temperaturas[ciudad][semana])):
                suma_temperaturas += temperaturas[ciudad][semana][dia]
                total_dias += 1

        # Calculamos el promedio para la ciudad
        if total_dias > 0:
            promedio_ciudad = suma_temperaturas / total_dias
            promedios_ciudades.append(promedio_ciudad)
        else:
            promedios_ciudades.append(None)  # Manejo de ciudad sin datos

    return promedios_ciudades
# Llamada a la función para calcular promedios
promedios = calcular_temperatura_promedio(temperaturas)

# Imprimir resultados
for i, promedio in enumerate(promedios):
    print(f"Promedio de temperatura para Ciudad {i + 1}: {promedio:.2f}")






