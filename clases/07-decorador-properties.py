class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property  # Indica al metodo de abajo que lo transforme a una propiedad
    def get_nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)
