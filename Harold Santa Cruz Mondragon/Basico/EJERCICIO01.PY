def saludar(nombre, saludo="Hola"):
    # Usamos f-string para formatear el texto y el parámetro por defecto 'saludo'
    print(f"{saludo}, {nombre}!")

# --- Pruebas ---
saludar("Ana")                 # Usa el saludo por defecto
# Salida: Hola, Ana!

saludar("Carlos", "Buenos días") # Sobrescribe el saludo por defecto
# Salida: Buenos días, Carlos!