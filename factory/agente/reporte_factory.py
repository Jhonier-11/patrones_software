from reporte import Reporte


class ReporteModelo(Reporte):
	def __init__(self, modelo: str):
		self.modelo = modelo

	def generar(self, datos: str) -> str:
		return f"Reporte generado con {self.modelo}: {datos}"

	def mostrar_info(self) -> None:
		print(f"Utilizando el modelo {self.modelo}")
