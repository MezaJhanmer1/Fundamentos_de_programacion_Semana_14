# EJERCICIO #01: SALUDO PERSONALIZADO

# Creamos la funcion
def saludar(nombre, saludo="Hola"):
    # Uso f-string para meter las variables dentro del texto usando las llaves
    print(f"{saludo}, {nombre}!")

# PRUEBAS

saludar("Luis")                 # Usa el saludo por defecto -> Hola, Luis!
saludar("Luis", "Buenos días")  # Pasamos ambos datos: 1ro nombre, 2do saludo -> Buenos días, Luis!