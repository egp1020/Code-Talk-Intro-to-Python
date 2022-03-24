personajes_dragon_ball = ["Gohan", "Goku", "Vegeta", "Trunks", "Piccolo", "Gohan"]

print(personajes_dragon_ball[0]) # Gohan
print(personajes_dragon_ball[1]) # Goku

dioses = ("griegos", "romanos", "nórdicos")

print(dioses[0]) # griegos
print(dioses[1]) # romanos
print(dioses[2]) # nórdicos

lista_dioses = list(dioses)
lista_dioses[0] = "Zeus"
dioses = tuple(lista_dioses)
print(dioses) # ("Zeus", "romanos", "nórdicos")
