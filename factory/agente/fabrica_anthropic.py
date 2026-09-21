from agente_fabrica import FabricaAgente
from consulta_ant import ConsultaAnthropic
from notificacion_factory import NotificacionModelo
from reporte_factory import ReporteModelo


class FabricaAnthropic(FabricaAgente):
    modelo = "anthropic"

    def crear_consulta(self):
        return ConsultaAnthropic()

    def crear_notificacion(self):
        return NotificacionModelo(self.modelo)

    def crear_reporte(self):
        return ReporteModelo(self.modelo)