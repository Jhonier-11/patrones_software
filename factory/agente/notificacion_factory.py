from notificacion import Notificacion


class NotificacionModelo(Notificacion):
	def __init__(self, modelo: str):
		self.modelo = modelo

	def enviar(self, mensaje: str) -> str:
		return f"Notificación enviada con {self.modelo}: {mensaje}"

	def mostrar_info(self) -> None:
		print(f"Utilizando el modelo {self.modelo}")
