# Lista de temperaturas
celsius = [10, 20, 30, 40]

# Convertir a Fahrenheit
fahrenheit = list(map(lambda x: x * 9/5 + 32, celsius))

# Mostrar temperaturas
print("Fahrenheit:", fahrenheit)


# Lista de numeros
numeros = [1, 2, 3, 4, 5, 6]

# Buscar numeros pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Mostrar pares
print("Numeros pares:", pares)


# Lista de precios
precios = [100, 50, 200, 30]

# Ordenar precios
ordenados = sorted(precios)

# Mostrar precios
print("Precios ordenados:", ordenados)