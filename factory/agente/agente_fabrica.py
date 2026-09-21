from abc import ABC, abstractmethod

from consulta import Consulta
from notificacion import Notificacion
from reporte import Reporte


class FabricaAgente(ABC):

	@abstractmethod
	def crear_consulta(self) -> Consulta:
		pass

	@abstractmethod
	def crear_notificacion(self) -> Notificacion:
		pass

	@abstractmethod
	def crear_reporte(self) -> Reporte:
		pass
