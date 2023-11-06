nombre_curso = "Ultimate Python" # String, cadena de caracteres, se puede abrir con ""/''
descripcion_curso = """
Ultimate Python,
Este curso contempla todos los detalles que necesitas
aprender para encontrar un trabajo como programador.
"""

#len : Nos ayuda a obtener la longitud del valor de nuestra variable en string.

print(len(nombre_curso))
print(nombre_curso[0]) # Accede al valor que esta posicionado el elemento en la variable, siempre se cuenta desde 0(cero)
print(nombre_curso[0:9]) # : indica desde que posicion inicial hasta posicion final
print(nombre_curso[9:]) # toma desde el indice 9 hasta el final
print(nombre_curso[:8]) # toma desde el indice 0 al 8
print(nombre_curso[:]) # toma tomo desde el 0 al final
 