# Importamos el módulo con el alias 'mu'
import matematicas_utils as mu

def reporte_geometrico(radios):
    # Imprimimos la cabecera de la tabla con formato
    print(f"{'Radio':<10} | {'Área':<15} | {'Perímetro':<15}")
    print("-" * 45)
    
    for r in radios:
        # Usamos las funciones del módulo importado
        area = mu.area_circulo(r)
        perimetro = mu.perimetro_circulo(r)
        
        # Imprimimos los datos formateados (:.<num>f limita los decimales)
        print(f"{r:<10.2f} | {area:<15.4f} | {perimetro:<15.4f}")

# --- Prueba ---
lista_radios = [1, 2.5, 5, 10]
reporte_geometrico(lista_radios)