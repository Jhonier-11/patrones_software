from inmueble import Inmueble


class Habitacion(Inmueble):

    def __init__(
        self,
        id,
        direccion,
        precio,
        bano_privado
    ):
        super().__init__(id, direccion, precio)
        self.bano_privado = bano_privado

    def mostrar_info(self):
        print(
            f"Habitación en {self.direccion} "
            f"- Precio: ${self.precio} "
            f"- Baño privado: {self.bano_privado}"
        )
