# EJERCICIO 03 : CLASIFICACION DE TEMPERATURA

def clasificar_temperatura(temp):      # Define la función y recibe 'temp'
    if temp < 10:                      # Si la temperatura es menor a 10
        return "Frío"                  # Devuelve "Frío"
    elif temp < 20:                    # Si no es <10, pero es menor a 20
        return "Fresco"                # Devuelve "Fresco"
    elif temp < 30:                    # Si no es <20, pero es menor a 30
        return "Cálido"                # Devuelve "Cálido"
    else:                              # Si no fue ninguna de las anteriores (es ≥30)
        return "Caliente"              # Devuelve "Caliente"

print(clasificar_temperatura(5))       # Llama a la función con 5 y lo muestra
print(clasificar_temperatura(15))      # Llama a la función con 15 y lo muestra
print(clasificar_temperatura(25))      # Llama a la función con 25 y lo muestra
print(clasificar_temperatura(35))      # Llama a la función con 35 y lo muestra