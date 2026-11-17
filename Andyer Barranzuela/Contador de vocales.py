# Crear un texto
texto = "Hola mundo"

# Crear un contador
contador = 0

# Revisar cada letra
for letra in texto:

    # Verificar si es una vocal
    if letra in "aeiouAEIOU":

        # Sumar una vocal
        contador = contador + 1

# Mostrar el resultado
print("Cantidad de vocales:", contador)