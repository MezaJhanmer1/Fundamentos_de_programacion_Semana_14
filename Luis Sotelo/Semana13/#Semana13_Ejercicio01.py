#Ejercicio01 - Saludo personalizado

def saludar(nombre, saludo="Hola"):      # nombre 1er parametro, #saludo 2do es opcional
  print(f"{saludo}, {nombre}!")          # print saludo + nombre!

saludar("Ana")                     # al existir un solo valor toma "nombre" y agrega el saludo por defecto al no darle un 2do dato ala funcion
saludar("Carlos", "Buenos días")        # al existir 2 valores, reemplaza el saludo por el actual.