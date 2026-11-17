# Ejercicio04 - Contador de vocales

def contar_vocales(texto):
  vocales = "aeiouáéíóú"
  contador = 0

  for letra in texto.lower():
    if letra in vocales:
      contador += 1

  return contador

print(contar_vocales("Messi es muy bueno"))  
print(contar_vocales("Archipiélago"))  
print(contar_vocales("COMPUTACIÓN"))  