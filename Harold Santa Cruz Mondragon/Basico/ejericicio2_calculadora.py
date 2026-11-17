def calcular(a, b, operador):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        # Validamos que b no sea 0 antes de dividir
        if b == 0:
            print("Error: No se puede dividir por cero.")
            return None
        else:
            return a / b
    else:
        print("Error: Operador no válido.")
        return None

print("Pruebas de la calculadora:")
print("ELIJA EL PRIMER NÚMERO:")
a = float(input())
print("ELIJA EL SEGUNDO NÚMERO:")
b = float(input())
print("ELIJA EL OPERADOR: +, -, *, /")
operador = input()
print(calcular(a, b, operador))
