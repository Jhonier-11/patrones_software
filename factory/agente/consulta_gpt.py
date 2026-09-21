from consulta import Consulta


class ConsultaGPT(Consulta):
	modelo = "gpt"

	def ejecutar(self, pregunta: str) -> str:
		return f"Respuesta de {self.modelo} para: {pregunta}"

	def mostrar_info(self) -> None:
		print(f"Utilizando el modelo {self.modelo}")
