# Ejercicio05 - Analizador de notas CSV

import csv
estudiantes = []
                                                                        # Abrir archivo csv, modo lectura y codificado para tildes y ñ
with open("estudiantes.csv", mode="r", encoding="utf-8") as archivo:    # --con with el archivo se cierra al terminar de usar.   
    lector = csv.DictReader(archivo)                                    # Convierte cada fila en un diccionario de Python
                                                                        # --toma la primera linea como encabezado
    for fila in lector:                                                 # ciclo for q recorrer por cada linea
        notas = [float(fila["nota1"]), float(fila["nota2"]), float(fila["nota3"])] # al ser csv estos datos son string, con el float 
        promedio = sum(notas) / len(notas)                                         # --pasamos a decimal.
        
        estudiantes.append({                                            # un dicc. nuevo con ("nombre" y "promedio") 
            "nombre": fila["nombre"],                                   # inserta al final de la lista estudiantes
            "promedio": promedio
        })

print("--- Promedio por alumno ---")
for est in estudiantes:
    print(f"{est['nombre']}: {est['promedio']:.2f}")

top_alumno = max(estudiantes, key=lambda x: x["promedio"])          #De cada ficha (x), fíjate solo en su "promedio" para decidir quién gana"
print(f"\nTop alumno: {top_alumno['nombre']} con promedio {top_alumno['promedio']:.2f}")

aprobados = sum(1 for est in estudiantes if est["promedio"] >= 13)
print(f"Total de aprobados (prom >= 13): {aprobados}")