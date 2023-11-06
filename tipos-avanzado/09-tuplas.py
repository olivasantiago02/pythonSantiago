# TUPLAS : no se pueden modificar, son como las listas

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])  # Recibe cualquier dato iterable
print(punto)

primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)
