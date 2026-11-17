def contadordevocales (texto):
    "funcion de contador de vocales"
    vocales = "aeiouáéíóú"
    contador = 0
    for letra in texto.lower():
        if letra in vocales:
            contador += 1
    return contador 
print("Ingrese un texto:")
texto = input()
print("El número de vocales en el texto es:", contadordevocales(texto))