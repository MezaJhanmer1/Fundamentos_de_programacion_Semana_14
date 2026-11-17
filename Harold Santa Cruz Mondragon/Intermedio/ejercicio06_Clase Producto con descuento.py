class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio actual."""
        if 0 <= porcentaje <= 100:
            descuento = self.precio * (porcentaje / 100)
            self.precio -= descuento
        else:
            print("Porcentaje de descuento no válido.")

    def vender(self, cant):
        """Resta stock y lanza error si no hay suficiente."""
        if cant > self.stock:
            # Lanzamos la excepción ValueError según lo solicitado
            raise ValueError(f"Stock insuficiente. Solo quedan {self.stock} unidades de {self.nombre}.")
        
        self.stock -= cant
        print(f"Venta exitosa: {cant} unidades de {self.nombre}.")

    def __str__(self):
        """Representación en texto del objeto para print()."""
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

# --- Pruebas ---
prod = Producto("Chocoton", 3.50, 300)
print(prod)  # Muestra el producto inicial

prod.aplicar_descuento(10) # 10% de descuento
print(prod)  # Muestra el producto con nuevo precio

prod.vender(3)
print(prod)  # Muestra el stock actualizado

# Esto lanzará el ValueError
try:
    prod.vender(5)
except ValueError as e:
    print(f"Error capturado: {e}")