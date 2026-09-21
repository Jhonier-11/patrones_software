from abc import ABC, abstractmethod


class Reporte(ABC):
	@abstractmethod
	def generar(self, datos: str) -> str:
		pass

	@abstractmethod
	def mostrar_info(self) -> None:
		pass
