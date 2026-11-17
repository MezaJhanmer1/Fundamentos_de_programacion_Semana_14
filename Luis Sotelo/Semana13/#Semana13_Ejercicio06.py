
# Ejercicio06 Clase Producto con descuento

class Producto:                                             # definir la clase producto

    def __init__(self, nombre, precio, stock):              # Constructor: inicializa atributos
        self.nombre = nombre                                # attr. de instancia guarda nombre
        self.precio = precio                                # attr. de instancia guarda precio
        self.stock = stock                                  # attr. de instancia guarda cant inicial de stock

    # funcion dentro de clase es METODO 
    def aplicar_descuento(self, pct):                       # método que recibe un porcentaje de descuento pct.
        monto_descuento = self.precio * (pct / 100)         # 250 *0.20 = 50               
        self.precio = self.precio - monto_descuento         # 250 - 50 = 200                                           
                                                    
    def vender(self, cantidad):                             # método para registrar venta según la cantidad solicitada.
        if cantidad > self.stock:                           # si el cliente pide más unidades de las que existen en el inventario.
            raise ValueError("Sin stock")                   # lanza excepcion tipo value error.
        self.stock -= cantidad                              # Si hay inventario, resta la cantidad vendida a "stock"
        return self.precio * cantidad                       # Calcula el monto total de la venta.

    def __str__(self):                                      # método especial indica cómo mostrarse el objeto cuando se convierte a texto
        return f"[{self.nombre}] S/.{self.precio:.2f}"

# --- PRUEBAS CON PRINT ---


p1 = Producto("Teclado Mecánico", 250.00, 10)                   # Creamos un producto (se ejecuta __init__)

print("Producto inicial:", p1)                                  # Imprimimos el objeto (se ejecuta __str__)
print("Stock disponible:", p1.stock)

p1.aplicar_descuento(20)                                        # Aplicamos un 20% de descuento y mostramos el cambio
print("Con 20% de descuento:", p1)                              

total_venta = p1.vender(3)                                      # Vendemos 3 unidades y mostramos cuánto se cobró y cuánto stock queda
print(f"Total cobrado por 3 unidades: S/.{total_venta:.2f}")
print("Stock restante:", p1.stock)

print("\nIntentando vender 15 unidades...")                     # Probamos el error cuando no hay stock suficiente
try:                                                            # Inicia un bloque vigilado para ejecutar código que podría lanzar un error sin que el programa se cierre bruscamente.
  p1.vender(15)                                                 # dispara el raise ValueError porq solo quedan 7.
except ValueError as e:
  print("Error detectado correctamente:", e)