from models.factory.inmueble_factory import InmuebleFactory


class ServicioArriendos:

    def registrar_inmueble(
        self,
        factory: InmuebleFactory,
        id,
        direccion,
        precio
    ):

        inmueble = factory.crear_inmueble(
            id,
            direccion,
            precio
        )

        return inmueble
