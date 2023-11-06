animal = "   chanCHito feliz   "
print(animal.upper()) #Toma el string dentro de la variable y transforma todo a letras mayusculas
print(animal.lower()) #Minuscula todas las letras
print(animal.capitalize()) #Mayuscula la primera letra y el resto deja minuscula
print(animal.title()) #Primera letra de cada palabra y las transf. a mayuscula
print(animal.strip()) #Remueve los espacios de la izq. y la derecha
print(animal.strip().title()) #Se pueden concatenar los metodos
print(animal.lstrip()) #elimina espacios de la izquierda
print(animal.rstrip()) #elimina espacios de la derecha
print(animal.find("CH")) #Busca cadena de caracteres en el string
print(animal.replace("nCH", "MAN")) #Remplaza la cadena de caracteres
print("nCH" in animal) #Busca coincidencias dentro del valor del string, devuelve True/False
print("nCH" not in animal) #Devuelve un boolean True/False
