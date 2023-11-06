class Animal:
    def comer(self):
        print("cominedo")


class Perro():

    def pasear(self):
        print("paseando")


class Chancito(Perro, Animal):

    def programar(self):
        print("programando")
