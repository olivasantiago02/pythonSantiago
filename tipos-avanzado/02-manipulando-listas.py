mascotas = ["wolfgang", "pelusa", "copito", "pulga"]
print(mascotas[0]) #Acceder al elemento de la lista
mascotas[0] = "Bicho" #Cambia el valor 0 del listado mascotas
print(mascotas[0:2]) #izq indice por cual va a recortar, der indice hasta donde llega
print(mascotas[-1]) #A valor negativo toma desde el cero a la izquierda
print(mascotas[::2]) #elige de la lista 1 por medio, par.

numeros = list(range(1, 21))
print(numeros[::2]) #par
print(numeros[1::2]) #impar
