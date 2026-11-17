# Importar el modulo
import matematicas_utils as mu

# Crear lista de radios
radios = [2, 4, 6]

# Recorrer los radios
for radio in radios:

    # Calcular area
    area = mu.area_circulo(radio)

    # Calcular perimetro
    perimetro = mu.perimetro_circulo(radio)

    # Mostrar resultados
    print("Radio:", radio)
    print("Area:", area)
    print("Perimetro:", perimetro)
    print("----------------")