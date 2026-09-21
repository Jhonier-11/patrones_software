from inmueble import Inmueble


class Apartamento(Inmueble):

    def __init__(self, id, direccion, precio, habitaciones):
        super().__init__(id, direccion, precio)
        self.habitaciones = habitaciones

    def mostrar_info(self):
        print(
            f"Apartamento en {self.direccion} "
            f"- Precio: ${self.precio} "
            f"- Habitaciones: {self.habitaciones}"
        )
