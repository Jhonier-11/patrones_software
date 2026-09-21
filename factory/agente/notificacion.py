
from abc import ABC, abstractmethod


class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> str:
        pass

    @abstractmethod
    def mostrar_info(self) -> None:
        pass