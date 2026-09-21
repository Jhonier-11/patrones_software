


from abc import ABC, abstractmethod


class Consulta(ABC):
    @abstractmethod
    def ejecutar(self, pregunta: str) -> str:
        pass

    @abstractmethod
    def mostrar_info(self) -> None:
        pass
