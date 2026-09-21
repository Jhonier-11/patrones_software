
from agente_fabrica import FabricaAgente


class Cliente:
    def __init__(self, fabrica: FabricaAgente):
        self._fabrica = fabrica

    def consultar(self, pregunta: str) -> str:
        return self._fabrica.crear_consulta().ejecutar(pregunta)

    def reporte(self, datos: str) -> str:
        return self._fabrica.crear_reporte().generar(datos)

    def notificar(self, mensaje: str) -> str:
        return self._fabrica.crear_notificacion().enviar(mensaje)
    