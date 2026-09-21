from abc import ABC, abstractmethod


class Inmueble(ABC):

    def __init__(self, id, direccion, precio):
        self.id = id
        self.direccion = direccion
        self.precio = precio

    @abstractmethod
    def mostrar_info(self):
        pass
