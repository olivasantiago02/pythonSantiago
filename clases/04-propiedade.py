class Perro:
    patas = 4

    def __init__(self, nombre, edad):  # Se inicia el constructor
        self.nombre = nombre  # se le pasan los parametros
        self.edad = edad

    def habla(self):
        print(f"{self.edad}Guau!")


Perro.patas = 2 #Se pueden cambiar las propiedades de clase mas abajo
mi_perro = Perro("Chanchito", 1)  # A LA 1ERA INSTANCIA LE CORRESPONDE NOMBRE
mi_perro2 = Perro("Felipe", 1)  # A LA 1ERA INSTANCIA LE CORRESPONDE NOMBRE
print(Perro.patas)
print(mi_perro2.patas)

