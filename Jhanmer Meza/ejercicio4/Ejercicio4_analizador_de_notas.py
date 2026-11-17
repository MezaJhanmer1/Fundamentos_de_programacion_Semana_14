
# Ejercicio 05 - Analizador de notas CSV

# Importar el módulo csv para leer archivos CSV
import csv

# Crear una lista para almacenar los estudiantes
estudiantes = []

# Abrir el archivo estudiantes.csv en modo lectura
with open("estudiantes.csv", "r", encoding="utf-8") as archivo:

    # Leer el archivo utilizando DictReader
    lector = csv.DictReader(archivo)

    # Recorrer cada fila del archivo
    for fila in lector:

        # Convertir las notas de texto a números decimales
        nota1 = float(fila["nota1"])
        nota2 = float(fila["nota2"])
        nota3 = float(fila["nota3"])

        # Calcular el promedio del estudiante
        promedio = (nota1 + nota2 + nota3) / 3

        # Guardar el nombre y el promedio en la lista
        estudiantes.append({
            "nombre": fila["nombre"],
            "promedio": promedio
        })


# Mostrar el promedio de cada estudiante
print("PROMEDIOS DE LOS ESTUDIANTES")

for alumno in estudiantes:
    print(alumno["nombre"], "-", round(alumno["promedio"], 2))


# Buscar al estudiante con el promedio más alto
mejor_alumno = max(estudiantes, key=lambda alumno: alumno["promedio"])

# Mostrar al estudiante con mejor promedio
print("\nMEJOR ALUMNO")
print("Nombre:", mejor_alumno["nombre"])
print("Promedio:", round(mejor_alumno["promedio"], 2))


# Crear un contador de alumnos aprobados
aprobados = 0

# Recorrer la lista de estudiantes
for alumno in estudiantes:

    # Comprobar si el promedio es mayor o igual a 13
    if alumno["promedio"] >= 13:
        aprobados += 1

# Mostrar la cantidad de aprobados
print("\nCantidad de alumnos aprobados:", aprobados)
