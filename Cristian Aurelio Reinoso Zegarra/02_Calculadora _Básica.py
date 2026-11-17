# Define la función 'calcular' que recibe 3 datos
def calcular(a, b, operador):
    
    # Si el operador es un signo de suma
    if operador == '+':
        return a + b                  # Retorna el resultado de la suma y termina la función.
        
    # Si es un signo de resta
    elif operador == '-':
        return a - b                  # Retorna la resta.
        
    # Si es un signo de multiplicación
    elif operador == '*':
        return a * b                  # Retorna la multiplicación.
        
    # Si es un signo de división
    elif operador == '/':
        # Primero verificamos que 'b'(el segundo numero) no sea cero.
        if b != 0:
            return a / b              # Si no es cero, hace la división normal.
        else:
            print("Error: No se puede dividir entre 0.") # Si es cero, muestra error.
            return None               # Retorna vacio para indicar que falló.
            
    # Si el usuario escribió cualquier otra cosa (ej. una letra o '$')...
    else:
        print("Error: Operador no válido.")   # Muestra error.
        return None                   # Retorna 'None' para indicar que falló.


# SOLICITAMOS LOS DATOS AL USUARIO 

# Pide un número, usamos 'float' para convertirlo a decimal.
num1 = float(input("Ingresa el primer número: "))

# Pide el operador. Aquí no usamos 'float' porque el operador es un texto
op = input("Ingresa el operador (+, -, *, /): ")

# Pide el segundo número y lo convierte a decimal.
num2 = float(input("Ingresa el segundo número: "))


# EJECUTAMOS LA FUNCIÓN Y MOSTRAMOS EL RESULTADO

# Llama a la función 'calcular'y guarda la respuesta en la variable 'resultado'.
resultado = calcular(num1, num2, op)

# Verifica si la operación fue exitosa y no hubo errores
if resultado is not None:
    # Imprime la operación completa y el resultado usando f-string.
    print(f"El resultado de {num1} {op} {num2} es: {resultado}")