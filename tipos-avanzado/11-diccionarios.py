punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])  # Accede al valor de x
print(punto["y"])  # Accede al valor de y

punto["z"] = 45

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del(punto["y"])


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"}
]

for usuario in usuarios:
    print(usuario["nombre"])
