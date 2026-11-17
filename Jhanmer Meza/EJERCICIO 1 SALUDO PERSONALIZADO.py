# Ejercicio 1 - Saludo personalizado

def saludar(nombre, saludo="Hola"):

    print(f"{saludo}, {nombre}!")

# Como no se indica un saludo, utiliza "Hola" por defecto
saludar("Andrey")

# En este caso, reemplaza el saludo por defecto, ya que mandamos 2 valores y el segundo es diferente
saludar("Andrey", "Buenos días")
