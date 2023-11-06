class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_name(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        # __nombre : Propiedad Privada no se pueden modificar
        print(f"{self.__nombre} dice : Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 4)


# ctrl + shift + p = rename symbol para privatizar la variable

perro1 = Perro.factory()
perro1.habla()
print(perro1.get_name())
