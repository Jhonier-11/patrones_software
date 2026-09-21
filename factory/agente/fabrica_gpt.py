from agente_fabrica import FabricaAgente
from consulta_gpt import ConsultaGPT
from notificacion_factory import NotificacionModelo
from reporte_factory import ReporteModelo


class FabricaGPT(FabricaAgente):
    modelo = "gpt"

    def crear_consulta(self):
        return ConsultaGPT()

    def crear_notificacion(self):
        return NotificacionModelo(self.modelo)

    def crear_reporte(self):
        return ReporteModelo(self.modelo)