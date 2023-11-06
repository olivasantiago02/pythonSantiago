class Perro:
    patas = 4

    def __init__(self, nombre, edad):  # Se inicia el constructor
        self.nombre = nombre  # se le pasan los parametros
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 4)


Perro.habla()
perro1 = Perro("Chanchito", 2)
perro2 = Perro("Felipe", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)

