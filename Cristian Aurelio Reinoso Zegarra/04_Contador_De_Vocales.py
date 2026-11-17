def contar_vocales(texto):                     # Define la función y recibe el texto
    texto = texto.lower()                      # Convierte todo a minúsculas
    vocales = "aeiouáéíóú"                     # Define las vocales (con tildes)
    contador = 0                               # Inicia el contador en 0
    for letra in texto:                        # Recorre el texto letra por letra
        if letra in vocales:                   # Si la letra está en la lista de vocales
            contador += 1                      # suma 1 al contador
    return contador                            # Devuelve el total contado

# SOLICITAMOS EL DATO AL USUARIO 
texto_usuario = input("Ingresa un texto: ")    # Pide al usuario que escriba algo

# EJECUTAMOS Y MOSTRAMOS
resultado = contar_vocales(texto_usuario)      # Llama a la función con el texto ingresado
print(f"El texto tiene {resultado} vocales.")  # Muestra el resultado final