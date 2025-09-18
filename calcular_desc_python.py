def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada a la función con monto total
    monto1 = 500  # Ejemplo de monto total
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}")

    print()  # Línea en blanco para separar resultados

    # Segunda llamada a la función con monto total y porcentaje de descuento
    monto2 = 245  # Otro ejemplo de monto total
    porcentaje2 = 15  # Porcentaje de descuento diferente
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")
