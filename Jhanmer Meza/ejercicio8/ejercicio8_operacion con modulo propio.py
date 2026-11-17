
# Ejercicio 08 - Importar módulo propio

# Importar el módulo matematicas_utils con el alias mu
import matematicas_utils as mu

# Crear una función que recibe una lista de radios
def reporte_geometrico(radios):

    # Mostrar el encabezado de la tabla
    print("REPORTE GEOMÉTRICO")
    print("---------------------------------------")
    print("Radio\tÁrea\t\tPerímetro")
    print("---------------------------------------")


    for r in radios:

        # Calcular el área utilizando el módulo importado
        area = mu.area_circulo(r)

        # Calcular el perímetro utilizando el módulo importado
        perimetro = mu.perimetro_circulo(r)

        # Mostrar los resultados en forma de tabla
        print(f"{r}\t{area:.2f}\t\t{perimetro:.2f}")


# Crear una lista con diferentes radios
radios = [2, 4, 6, 8]


reporte_geometrico(radios)
