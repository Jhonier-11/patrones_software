from service.servicio_arriendo import ServicioArriendos

from models.factory.apartamento_factory import ApartamentoFactory
from models.factory.habitacion_factory import HabitacionFactory
from models.factory.casa_factory import CasaFactory


def main():

    servicio = ServicioArriendos()

    apartamento_factory = ApartamentoFactory()
    habitacion_factory = HabitacionFactory()
    casa_factory = CasaFactory()

    apartamento = servicio.registrar_inmueble(
        apartamento_factory,
        1,
        "Barrio Las Flores",
        850000
    )

    habitacion = servicio.registrar_inmueble(
        habitacion_factory,
        2,
        "Barrio Novalito",
        450000
    )

    casa = servicio.registrar_inmueble(
        casa_factory,
        3,
        "Barrio Los Cortijos",
        1200000
    )

    apartamento.mostrar_info()
    habitacion.mostrar_info()
    casa.mostrar_info()


if __name__ == "__main__":
    main()
