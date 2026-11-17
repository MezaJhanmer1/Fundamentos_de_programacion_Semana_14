# Importar csv
import csv

# Abrir archivo
archivo = open("estudiantes.csv", "r")

# Leer alumnos
datos = csv.DictReader(archivo)

# Crear contador
aprobados = 0

# Recorrer alumnos
for alumno in datos:

    # Obtener nombre y nota
    nombre = alumno["nombre"]
    nota = float(alumno["prom"])

    # Mostrar alumno
    print(nombre, nota)

    # Contar aprobados
    if nota >= 13:
        aprobados += 1

# Mostrar aprobados
print("Aprobados:", aprobados)

# Cerrar archivo
archivo.close()