class Perro:
    def __init__(self, nombre, edad): #Se inicia el constructor
        self.nombre = nombre #se le pasan los parametros
        self.edad = edad
    def habla(self):
        print(f"{self.edad}Guau!")


mi_perro = Perro("Chanchito", 1) # A LA 1ERA INSTANCIA LE CORRESPONDE NOMBRE
# mi_perro2 = Perro("Felipe") # A LA SEGUNDA INSATNCIA LE CORRESPONDE NOMBRE
print(mi_perro.nombre) # Variable 1 = Chanchito
# print(mi_perro2.nombre) # Variable 2 = Felipe
