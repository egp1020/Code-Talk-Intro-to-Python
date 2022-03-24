# Forma

""" if condicion:
    codigo
elif condicion:
    codigo
else:
    codigo
# Nota: puede ir un if """

# Ejemplo

tiene_nave = True
tiene_combustible = True

if tiene_nave and tiene_combustible:
    print("¡Puede atacar!")
elif tiene_nave and not tiene_combustible:
    print("¡Puede aterrizar!")
else:
    print("¡No puede atacar ni aterrizar!")