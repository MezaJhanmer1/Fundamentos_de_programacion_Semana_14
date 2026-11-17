# Ejercicio02 - Calculadora básica

def calcularOpe(a, b, operador):
  if operador == "+":
    return a + b
  elif operador == "-":
    return a - b
  elif operador == "*":
    return a * b
  elif operador == "/":
    if b == 0:
      print("Error: No se puede dividir por cero.")
      return None
    return a / b
  else:
    print("Error: Operador no válido.")
    return None


print(calcularOpe(20, 5, "+")) 
print(calcularOpe(22, 0, "/"))  
print(calcularOpe(100, 5, "%"))  