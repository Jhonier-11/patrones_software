from models.apartamento import Apartamento
from models.habitacion import Habitacion
from models.casa import Casa


class ServicioArriendos:

    def crear_inmueble(
        self,
        tipo,
        id,
        direccion,
        precio
    ):

        if tipo == "apartamento":

            return Apartamento(
                id,
                direccion,
                precio,
                3
            )

        elif tipo == "habitacion":

            return Habitacion(
                id,
                direccion,
                precio,
                True
            )

        elif tipo == "casa":

            return Casa(
                id,
                direccion,
                precio,
                4
            )

        else:
            raise ValueError(
                "Tipo de inmueble no válido"
            )
