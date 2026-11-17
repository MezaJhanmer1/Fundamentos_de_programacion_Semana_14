#Ejercicio08 - Importar módulo propio

import matematicas_utils as mu              # Busca un archivo llamado matematicas_utils.py en la misma carpeta y carga sus func. 
                                            # (mu) para no tener que escribir el nombre largo cada vez que uses una de sus func.


def reporte_geometrico(radios: list):                           # func rep.. espera recibir lista(radios). 
                                                                # list sirve como ayuda visual para indicar el tipo de dato esperado.
  print(f"{'Radio':<10} | {'Área':<12} | {'Perímetro':<12}")     # Encabezado de la tabla con alineación de columnas
  print("-" * 40)

  
  for r in radios:                                              # Recorremos cada radio y usamos las funciones del módulo importado
    area = mu.area_circulo(r)
    perimetro = mu.perimetro_circulo(r)
    print(f"{r:<10.2f} | {area:<12.2f} | {perimetro:<12.2f}")


lista_radios = [1, 2.5, 5, 10]
reporte_geometrico(lista_radios)