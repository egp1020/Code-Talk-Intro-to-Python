#----------------------------------------
# Crear una lista
#----------------------------------------

nombre_lista = []
nombre_lista = list()
nombre_lista = ["elementos"]

#----------------------------------------
# Métodos comunes
#----------------------------------------

personajes_dragon_ball = ["Gohan", "Goku", "Vegeta", "Trunks", "Piccolo", "Gohan"]

# append
personajes_dragon_ball.append("Bulma")
print(personajes_dragon_ball) # ["Gohan", "Goku", "Vegeta", "Trunks", "Piccolo", "Gohan", "Bulma"]

# remove
personajes_dragon_ball.remove("Goku")
print(personajes_dragon_ball) # ["Gohan", "Vegeta", "Trunks", "Piccolo", "Gohan", "Bulma"]

# pop
personajes_dragon_ball.pop()
print(personajes_dragon_ball) # ["Gohan", "Vegeta", "Trunks", "Piccolo", "Gohan"]

# sort
personajes_dragon_ball.sort() # ordena listas con el mismo tipo de dato.
print(personajes_dragon_ball) # ["Gohan", "Gohan", "Piccolo", "Trunks", "Vegeta"]

# reverse
personajes_dragon_ball.reverse()
print(personajes_dragon_ball) # ["Vegeta", "Trunks", "Piccolo", "Gohan", "Gohan"]

# count
veces = personajes_dragon_ball.count("Gohan")
print(veces) # 2


