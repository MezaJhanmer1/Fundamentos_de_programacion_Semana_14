# Funcion para clasificar la temperatura
def temperatura(temp):

    # Si es menor que 10
    if temp < 10:
        return "Frio"

    # Si es menor que 20
    elif temp < 20:
        return "Fresco"

    # Si es menor que 30
    elif temp < 30:
        return "Calido"

    # Si es 30 o mayor
    else:
        return "Caliente"


# Mostrar resultados
print(temperatura(5))
print(temperatura(15))
print(temperatura(25))
print(temperatura(35))