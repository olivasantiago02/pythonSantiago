class Animal:
    def comer(self):
        print("cominedo")


class Perro(Animal): #Herencia: Toma todos los valores/propiedades
    def pasear(self):
        print("paseando")

class Chancito(Perro): #Herencia Multi-Nivel: Hereda de las dos Clases Perro y Animal

    def programar(self):
        print("programando")
