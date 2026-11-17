def temperatura_clasificador(temperatura):
    if 0 <= temperatura < 10:
        return "Frío"
    elif 10 <= temperatura < 20:
        return "Templado"
    elif 20 <= temperatura < 30:
        return "Cálido"
    else:
        return "Caliente"
print("Ingrese la temperatura en grados Celsius:")
temperatura = float(input())
print(temperatura_clasificador(temperatura))