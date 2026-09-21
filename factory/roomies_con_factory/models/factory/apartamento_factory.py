from inmueble_factory import InmuebleFactory
from apartamento import Apartamento


class ApartamentoFactory(InmuebleFactory):

    def crear_inmueble(
        self,
        id,
        direccion,
        precio
    ):

        return Apartamento(
            id,
            direccion,
            precio,
            3
        )
