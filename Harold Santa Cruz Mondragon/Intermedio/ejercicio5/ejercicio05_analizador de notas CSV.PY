import csv

def analizar_notas(estudiantes_csv):
    alumnos = []
    
    try:
        with open(estudiantes_csv, mode='r', encoding='utf-8') as archivo:
            # Usamos DictReader para acceder a las columnas por su nombre
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                # Calculamos el promedio (asumiendo 3 notas)
                try:
                    n1 = float(fila['nota1'])
                    n2 = float(fila['nota2'])
                    n3 = float(fila['nota3'])
                    promedio = (n1 + n2 + n3) / 3
                    
                    alumnos.append({
                        'nombre': fila['nombre'],
                        'promedio': promedio
                    })
                except ValueError:
                    print(f"Error en los datos de {fila.get('nombre', 'Desconocido')}")
                    continue
                    
    except FileNotFoundError:
        print(f"El archivo {estudiantes_csv} no existe.")
        return

    if not alumnos:
        print("No se encontraron datos válidos.")
        return

    # 1. Encontrar al top alumno usando max() y lambda
    top_alumno = max(alumnos, key=lambda x: x['promedio'])
    
    # 2. Contar aprobados (promedio >= 13)
    # Usamos una expresión generadora para contar de forma eficiente
    aprobados = sum(1 for alumno in alumnos if alumno['promedio'] >= 13)
    
    # Mostrar resultados
    print(f"Top alumno: {top_alumno['nombre']} (Promedio: {top_alumno['promedio']:.2f})")
    print(f"Cantidad de aprobados (>=13): {aprobados}")
# Al final de tu archivo, agrega esto:
analizar_notas('semana14/estudiantes.csv')