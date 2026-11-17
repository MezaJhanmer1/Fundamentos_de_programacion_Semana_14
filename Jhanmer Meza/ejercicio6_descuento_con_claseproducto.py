# Ejercicio 06 - Clase Producto con descuento

# Crear la clase Producto
class Producto:

    # Constructor: inicializar los atributos del producto
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Método para aplicar un descuento al precio
    def aplicar_descuento(self, porcentaje):

        # Calcular el nuevo precio con el descuento
        self.precio = self.precio - (self.precio * porcentaje / 100)

    # Método para vender una cantidad de productos
    def vender(self, cant):

        # Comprobar si hay suficiente stock
        if cant > self.stock:
            raise ValueError("Error: No hay suficiente stock")

        # Restar la cantidad vendida del stock
        self.stock -= cant

        # Mostrar un mensaje de venta
        print("Venta realizada correctamente")

    # Método para mostrar la información del producto
    def __str__(self):

        # Retornar los datos del producto como texto
        return f"Producto: {self.nombre} | Precio: S/{self.precio:.2f} | Stock: {self.stock}"


# Crear un objeto de la clase Producto
producto1 = Producto("Laptop", 2500, 10)

# Mostrar la información inicial del producto
print(producto1)

# Aplicar un descuento del 10%
producto1.aplicar_descuento(10)

# Mostrar el producto con el nuevo precio
print("\nDespués del descuento:")
print(producto1)

# Vender 3 unidades del producto
producto1.vender(3)

# Mostrar el stock actualizado
print("\nDespués de la venta:")
print(producto1)
