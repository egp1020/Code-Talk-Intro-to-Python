""" # Forma

variable_resultado = condicion_verdadera if condicion else condicion_falsa
"""

# Ejemplo
en_batalla = True
nave_atacada = True

accion_realizar = "¡Debe aterrizar!" if en_batalla and nave_atacada else "¡Puede contraatacar!"
print(accion_realizar) # ¡Debe aterrizar!