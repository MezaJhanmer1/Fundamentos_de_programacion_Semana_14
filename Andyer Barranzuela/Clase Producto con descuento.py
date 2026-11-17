# Crear clase
class Producto:

    # Guardar datos
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Aplicar descuento
    def aplicar_descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * porcentaje / 100)

    # Vender producto
    def vender(self, cantidad):

        # Revisar stock
        if cantidad > self.stock:
            raise ValueError("No hay stock")

        # Descontar cantidad
        self.stock = self.stock - cantidad

    # Mostrar producto
    def __str__(self):
        return self.nombre


# Crear producto
producto = Producto("Laptop", 2000, 10)

# Aplicar descuento
producto.aplicar_descuento(10)

# Vender dos unidades
producto.vender(2)

# Mostrar resultados
print("Producto:", producto)
print("Precio:", producto.precio)
print("Stock:", producto.stock)