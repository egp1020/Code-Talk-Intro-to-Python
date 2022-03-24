# Forma - while

""" while condicion:
    # Acciones """

# Forma - for

""" for elemento in iterable:
    # Acciones"""

# Ejemplo - while
atacamos = True
municion = 10

""" while atacamos:
    print("Enemigo detectado")
    if municion > 0:
        print("Dispara")
        municion -= 1
    else:
        print("No hay munición. ¡Huye!")
        atacamos = False """

municion = 10

print("¡Enemigos a la vista!")
for enemigo in range(0, municion, 1):
    print(f"Enemigo {enemigo+1} muerto.")

