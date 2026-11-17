# Funcion para realizar operaciones
def calcular(a, b, operador):

    # Si el operador es suma
    if operador == "+":
        return a + b

    # Si el operador es resta
    elif operador == "-":
        return a - b

    # Si el operador es multiplicacion
    elif operador == "*":
        return a * b

    # Si el operador es division
    elif operador == "/":

        # Verificar que no sea cero
        if b != 0:
            return a / b
        else:
            return "No se puede dividir entre cero"

    # Si el operador no existe
    else:
        return "Operacion incorrecta"


# Mostrar los resultados
print(calcular(10, 5, "+"))
print(calcular(10, 5, "-"))
print(calcular(10, 5, "*"))
print(calcular(10, 5, "/"))