print("Hola Mundo")  # Imprime string en la consola


"""
(1)DEF : Para definir una funcion en Python
(2)HOLA: Le sigue el nombre de la variable
(3) (): abre la funcion y le siguen los :

() : Lo que le pasamos como "nombre" se denomina parametro
"""


def hola(nombre, apellido="Feliz"):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")
    


hola("Santiago", "Oliva") #Argumento se denomina asi a la variable que se le agrega un valor
hola("Chanchito")
#Parametro: Se denomina a la variable que se declara en la funcion

hola(apellido="schurmann", nombre="Wolfgang")
#De esta manera podemos indicarle cual es apellido y cual es nombre