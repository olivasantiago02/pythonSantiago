from abc import ABC, abstractmethod


class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(123)
