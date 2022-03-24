"""Crea una card ficticia de ti (imagina que eres un personaje de tu
   videojuego/pelicula/libro favorito). Luego muestra los datos de la
   card y su respectivo tipo de dato."""

nombre = "Jinx"
edad = 18
altura_m = 1.57
peso_kg = 49.9
tiene_pareja = False
caracteristicas = ["Veloz", "Crea bombas", "Support", "Difícil de controlar"]
descripcion_fisica = ("Delgada", "Cabello rojo", "Morena", "Tiene pecas")
hobbies = {"Jugar",
           "Dormir",
           "Comer",
           "Creas nuevas armas"}

card_personaje_datos = {
    "nombre":nombre,
    "edad":edad,
    "altura":altura_m,
    "peso":peso_kg,
    "pareja":tiene_pareja,
    "caracteristicas":caracteristicas,
    "descripcion_fisica":descripcion_fisica,
    "hobbies":hobbies
}

card_personaje_tipo_dato = {
    "nombre":type(nombre),
    "edad":type(edad),
    "altura":type(altura_m),
    "peso":type(peso_kg),
    "pareja":type(tiene_pareja),
    "caracteristicas":type(caracteristicas),
    "descripcion_fisica":type(descripcion_fisica),
    "hobbies":type(hobbies),
    "card":type(card_personaje_datos)
}

print(f"Tipos de datos: {card_personaje_tipo_dato}") # Tipos de datos: {'nombre': <class 'str'>, 'edad': <class 'int'>, 'altura': <class 'float'>, 'peso': <class 'float'>, 'pareja': <class 'bool'>, 'caracteristicas': <class 'list'>, 'descripcion_fisica': <class 'tuple'>, 'hobbies': <class 'list'>, 'card': <class 'dict'>}

print(f"Datos del personaje: {card_personaje_datos}\n") # Datos del personaje: {'nombre': 'Jinx', 'edad': 18, 'altura': 1.57, 'peso': 49.9, 'pareja': False, 'caracteristicas': ['Veloz', 'Crea bombas', 'Support', 'Difícil de controlar'], 'descripcion_fisica': ('Delgada', 'Cabello rojo', 'Morena', 'Tiene pecas'), 'hobbies': ['Jugar', 'Dormir', 'Comer', 'Creas nuevas armas']}






