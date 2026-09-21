from fabrica_anthropic import FabricaAnthropic
from fabrica_gpt import FabricaGPT
from servicio_agente import Cliente


def usar_cliente(fabrica):
	cliente = Cliente(fabrica)
	print(cliente.consultar(f"Esto es una consulta de prueba para {fabrica.modelo}"))
	print(cliente.notificar(f"Notificacion de prueba a {fabrica.modelo}"))
	print(cliente.reporte(f"Reporte de prueba para {fabrica.modelo}"))


if __name__ == "__main__":
	usar_cliente(FabricaGPT())
	usar_cliente(FabricaAnthropic())
