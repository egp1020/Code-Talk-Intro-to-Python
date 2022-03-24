"""Dada la velocidad de la luz, la velocidad máxima de flash y
   la velocidad máxima de superman; calcular cuántas veces es
   mayor la velocidad de flash y de superman a la velocidad de
   la luz. Además, decir si la velocidad de flash es mayor a la
   velocidad de superman.
"""


#Velocidad de la luz
VELOCIDAD_LUZ_KM_H = 1.08e+9

#Velocidad máxima de flash
velocidad_max_flash_km_h = 1.404e+22

#Velocidad máxima de superman
velocidad_max_superman_km_h = 5.616e+16

# Veces la velocidad de flash es mayor a la velocidad de la luz
veces_flash_luz= velocidad_max_flash_km_h // VELOCIDAD_LUZ_KM_H

# Veces la velocidad de superman es mayor a la velocidad de la luz
veces_superman_luz = velocidad_max_superman_km_h // VELOCIDAD_LUZ_KM_H

# Ganador
print("El ganador es Flash")