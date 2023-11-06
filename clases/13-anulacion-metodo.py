class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("Vuela vuela")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = True

    def vuela(self):
        super().vuela()  # Ejecuta el metodo de vuela de Ave primero por el orden
        print("vuela Pato")


pato = Pato()
pato.vuela()
