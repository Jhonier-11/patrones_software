from abc import ABC, abstractmethod


class InmuebleFactory(ABC):

    @abstractmethod
    def crear_inmueble(
        self,
        id,
        direccion,
        precio
    ):
        pass
