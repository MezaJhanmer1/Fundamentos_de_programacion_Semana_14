"""
matematicas_utils.py
--------------------
Módulo utilitario de funciones matemáticas.
Usado como ejemplo en la clase de Módulos y Organización del Código.
"""

import math


# ──────────────────────────────────────────────
# CONSTANTE del módulo
PI = 3.141592653589793
# ──────────────────────────────────────────────


def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    return PI * radio ** 2          # π × r²


def perimetro_circulo(radio: float) -> float:
    """Calcula el perímetro (circunferencia) de un círculo."""
    return 2 * PI * radio           # 2πr


def area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    return base * altura            # b × h


def es_primo(n: int) -> bool:
    """Devuelve True si n es un número primo."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def factoriales(limite: int) -> list:
    """Retorna una lista con los factoriales de 0 hasta 'limite'."""
    resultado = []
    for i in range(limite + 1):
        resultado.append(math.factorial(i))
    return resultado


def potencia(base: float, exponente: int = 2) -> float:
    """Eleva 'base' a 'exponente'. Por defecto, eleva al cuadrado."""
    return base ** exponente


# ── Bloque de prueba: solo se ejecuta si corres este archivo directamente ──
if __name__ == "__main__":
    print("=== Prueba de matematicas_utils ===")
    print(f"Área círculo r=5 : {area_circulo(5):.4f}")
    print(f"¿7 es primo?      : {es_primo(7)}")
    print(f"Factoriales 0-5   : {factoriales(5)}")
    print(f"3^4               : {potencia(3, 4)}")
