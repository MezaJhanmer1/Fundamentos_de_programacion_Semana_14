
# Ejercicio 04 - Contador de vocales


def contar_vocales(texto):

    # Convertir todo el texto a minúsculas
    texto = texto.lower()

    # Crear una variable para contar las vocales
    contador = 0

    # Recorrer cada letra del texto
    for i in texto:

        # Comprobar si la letra es una vocal, incluyendo las tildes
        if i in "aeiouáéíóú":
            contador += 1

    # Retornar la cantidad de vocales encontradas
    return contador


texto_usuario = input("Ingrese un texto: ")

resultado = contar_vocales(texto_usuario)

print("Cantidad de vocales:", resultado)
