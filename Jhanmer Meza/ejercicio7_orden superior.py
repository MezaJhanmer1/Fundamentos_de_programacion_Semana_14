
# Ejercicio 07 - Funciones de orden superior


temperaturas = [0, 10, 20, 30, 40]

# Convertir Celsius a Fahrenheit utilizando map()
fahrenheit = list(map(lambda x: (x * 9/5) + 32, temperaturas))

# Mostrar las temperaturas convertidas
print("Temperaturas en Fahrenheit:", fahrenheit)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar solamente los números pares utilizando filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Números pares:", pares)


# Crear una lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Carlos", "nota": 15},
    {"nombre": "Maria", "nota": 18},
    {"nombre": "Andrey", "nota": 12},
    {"nombre": "Lucia", "nota": 20}
]

# Ordenar los estudiantes por nota de menor a mayor
ordenados = sorted(estudiantes, key=lambda alumno: alumno["nota"])

print("Estudiantes ordenados por nota:", ordenados)
