
# Ejercicio 03 - Clasificador de temperatura

# Crear una función que recibe la temperatura
def clasificar_temperatura(temp):

    # Comprobar si la temperatura es menor que 10
    if temp < 10:
        return "Frío"

    # Comprobar si la temperatura es menor que 20
    elif temp < 20:
        return "Fresco"

    # Comprobar si la temperatura es menor que 30
    elif temp < 30:
        return "Cálido"

    # Si la temperatura es 30 o mayor
    else:
        return "Caliente"


# Solicitar al usuario que ingrese la temperatura
temperatura = float(input("Ingrese la temperatura: "))

resultado = clasificar_temperatura(temperatura)

print("La temperatura se clasifica como:", resultado)
