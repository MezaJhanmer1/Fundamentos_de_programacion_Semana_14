
#Ejercicio# 07 - Funciones de orden superior

celsius = [0, 15, 25, 30, 100]                                      # función q recibe un número c y aplica la formula 
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))         # lambda func no necesitas reutilizar en resto del código en vez de def.
                                                                    # map aplica la funcion a cada elemento sin aplicar bucle "for".
print("Celsius:", celsius)                                          # list Convierte el resultado de map (objeto especial) a una lista normal
print("Fahrenheit:", fahrenheit)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                            
pares = list(filter(lambda n: n % 2 == 0, numeros))          # función recibe num "n"; devuelve "True" si "/"es cero(par) o False es impar
print("\nNúmeros:", numeros)                                 # Evalúa cada número de lista y hace pasar los q cumplen la condicion
print("Solo pares:", pares)


productos = [                                               # lista q contiene diccionarios
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Teclado", "precio": 220},
    {"nombre": "USB", "precio": 35},
]
productos_ordenados = sorted(productos, key=lambda p: p["precio"])   # lambda cada dicc p, extrae únicamente "precio" y los ordena de < a >
print("\nProductos ordenados por precio (menor a mayor):")           # sorted devuelve nueva lista ordenada con los elementos de producto.
print(productos_ordenados)





# lambda c: (c * 9 / 5) + 32: pequeña función anónima q recibe un número c y aplica la fórmula de conversión a Fahrenheit.
# map(..., celsius): Toma función y la aplica automáticamente a cada elemento de la lista celsius, uno por uno.
# list(...): Convierte el resultado de map (que es un objeto especial) de vuelta a una lista normal y la guarda en fahrenheit.