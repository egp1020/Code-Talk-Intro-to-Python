# Ejemplo implícito

edad_tierra = 4.5e+9
print("Tipo de dato de la edad de la Tierra: ", type(edad_tierra)) # <class 'float'>

edad_yoda = 900
print("Tipo de dato de la edad de Yoda",type(edad_yoda)) # <class 'int'>

veces_edad_yoda_tierra = edad_tierra / edad_yoda # Casting implícito

print(f"La Tierra tiene {veces_edad_yoda_tierra} de veces la edad que Yoda.") # La Tierra tiene 5000000.0 más edad que Yoda.
print("Tipo de dato de las veces:", type(veces_edad_yoda_tierra)) # <class 'float'>


# Ejemplo de implícito y explícito

"""Han encontrado un sistema planetario, pero aún no le asignan nombre a sus planetas. Como eres un aventurero
   galáctico te han delegado la tarea. Para ello, debes dedicar una nombre base (el que tendrá todos los planetas)
   y, seguido de un guión medio, el número correspondiente a cada planeta.

   Ejemplo: Kepler-008, donde Kepler es el nombre base y 001 es el número."""

base = input("Ingrese el nombre base: ") # Moraband
numero_planeta_deseado = int(input("Ingrese el número del planeta deseado: ")) # 707

# Casting explícito
nombre_planeta = base + '-' + str(numero_planeta_deseado)

print(f"Tipo de dato (explícito): {type(nombre_planeta)}") # Tipo de dato (explícito): <class 'str'>
print(nombre_planeta) # Moraband-707

nombre_planeta = base + '-' + numero_planeta_deseado # TypeError: can only concatenate str (not "int") to str

# Casting implícito
nombre_planeta = f"{base}-{numero_planeta_deseado}"
print(f"Tipo de dato (implícito): {type(nombre_planeta)}") # Tipo de dato (implícito): <class 'str'>



