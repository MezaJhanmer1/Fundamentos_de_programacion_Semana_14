

# Ejercicio 02 - Calculadora básica

# Crear una función que recibe dos números y un operador
def calcular(a, b, operador):

    # Comprobar si el operador es suma
    if operador == "+":
        return a + b

    # Comprobar si el operador es resta
    elif operador == "-":
        return a - b

    # Comprobar si el operador es multiplicación
    elif operador == "*":
        return a * b

    # Comprobar si el operador es división
    elif operador == "/":

        # Verificar que el segundo número no sea cero
        if b != 0:
            return a / b
        else:
            print("Error: No se puede dividir entre cero")
            return None

    # Si el operador no es válido
    else:
        print("Error: Operador no válido")
        return None


# Solicitar los datos al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador (+, -, *, /): ")

# Llamar a la función y guardar el resultado
resultado = calcular(numero1, numero2, operador)

# Mostrar el resultado si es válido
if resultado is not None:
    print("El resultado es:", resultado)
