# 1. map() - Convertir temperaturas
celsius = [0, 10, 20, 30, 40]
# Fórmula: (C * 9/5) + 32
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Fahrenheit:", fahrenheit)

# 2. filter() - Solo números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

# 3. sorted() - Ordenar lista de diccionarios por un campo
personas = [
    {"nombre": "Zully", "edad": 23},
    {"nombre": "Leyle", "edad": 29},
    {"nombre": "Guilberto", "edad": 68}
]
# Ordenamos por edad de menor a mayor
ordenados_por_edad = sorted(personas, key=lambda p: p['edad'])
print("Ordenados por edad:", ordenados_por_edad)