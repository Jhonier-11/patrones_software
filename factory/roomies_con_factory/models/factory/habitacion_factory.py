from inmueble_factory import InmuebleFactory
from habitacion import Habitacion


class HabitacionFactory(InmuebleFactory):

    def crear_inmueble(
        self,
        id,
        direccion,
        precio
    ):

        return Habitacion(
            id,
            direccion,
            precio,
            True
        )
