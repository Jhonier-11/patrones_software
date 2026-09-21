from inmueble_factory import InmuebleFactory
from casa import Casa


class CasaFactory(InmuebleFactory):

    def crear_inmueble(
        self,
        id,
        direccion,
        precio
    ):

        return Casa(
            id,
            direccion,
            precio,
            4
        )
