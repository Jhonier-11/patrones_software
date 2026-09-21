from service.servicio_arriendo import ServicioArriendos


def main():

    servicio = ServicioArriendos()

    apartamento = servicio.crear_inmueble(
        "apartamento",
        1,
        "Barrio Las Flores",
        850000
    )

    habitacion = servicio.crear_inmueble(
        "habitacion",
        2,
        "Barrio Novalito",
        450000
    )

    casa = servicio.crear_inmueble(
        "casa",
        3,
        "Barrio Los Cortijos",
        1200000
    )

    apartamento.mostrar_info()
    habitacion.mostrar_info()
    casa.mostrar_info()


if __name__ == "__main__":
    main()
