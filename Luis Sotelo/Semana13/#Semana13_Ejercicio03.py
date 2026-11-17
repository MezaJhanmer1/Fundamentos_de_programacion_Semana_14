#Ejercicio03 - Clasificador de temperatura

def tipo_temperatura(temp):
  if temp < 10:
    return "Frío"
  elif temp < 20:
    return "Fresco"
  elif temp < 30:
    return "Cálido"
  else:
    return "Caliente"

print(tipo_temperatura(4))  
print(tipo_temperatura(13))  
print(tipo_temperatura(26))  
print(tipo_temperatura(35))  