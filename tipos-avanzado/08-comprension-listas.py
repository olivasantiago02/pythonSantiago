usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

"""
nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)
"""
#Map:
nombres = [usuario[0] for usuario in usuarios]
print(nombres)
