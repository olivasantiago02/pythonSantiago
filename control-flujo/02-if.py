"""
Las evaluaciones se hacen desde arriba hacia abajo
Primero el if evalua en True or Flase, si evalua en True no evalua lo siguiente
si la edad es mayor a 54 ejecuta el print del if
Luego evalua el elif si la edad es mayor a 17 accede al print
y por ultimo evalua el else el cual al acertar la 
afirmacion utiliza el print
"""

edad = 22
if edad > 54:
    print("Puede ver la pelicula con descuento")
elif edad > 17:
    print("Puedes ver la pelicula")
else:
    print("No puedes entrar")


print("Listo")
