tiene_poderes = True
quiere_ser_el_capitan = False

# and
respuesta = tiene_poderes and quiere_ser_el_capitan
print(f"¿Tiene poderes y quiere ser el capitan?: {respuesta}") # ¿Tiene poderes y quiere ser el capitan?: False

# or
respuesta = tiene_poderes or quiere_ser_el_capitan
print(f"¿Tiene poderes o quiere ser el capitan?: {respuesta}") # ¿Tiene poderes o quiere ser el capitan?: True

# not
respuesta = not tiene_poderes
print(f"¿Tiene poderes?: {respuesta}") # ¿Tiene poderes?: False