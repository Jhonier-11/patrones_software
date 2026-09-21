from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    La clase «Creator» declara el método de fábrica que debe devolver un
    objeto de la clase «Product». Las subclases de «Creator» suelen proporcionar la
    implementación de este método.
    """

    @abstractmethod
    def factory_method(self):
        """
        Ten en cuenta que el «Creator» también puede proporcionar alguna implementación predeterminada del
        método de fábrica.
        """
        pass

    def some_operation(self) -> str:
        """
        Ten en cuenta también que, a pesar de su nombre, la responsabilidad principal del «Creator»
        no es crear productos. Por lo general, contiene cierta lógica de negocio fundamental
        que se basa en objetos «Product», devueltos por el método «factory».
        Las subclases pueden modificar indirectamente esa lógica de negocio sobrescribiendo el
        método «factory» y devolviendo desde él un tipo diferente de producto.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: El mismo código del creador acaba de funcionar con {product.operation()}"

        return result


"""
Los «Concrete Creators» sobrescriben el método «factory» para cambiar el
tipo del producto resultante.
"""


class ConcreteCreator1(Creator):
    """
    Ten en cuenta que la firma del método sigue utilizando el tipo de producto abstracto,
    aunque en realidad el método devuelva el producto concreto. De esta
    forma, el creador puede mantenerse independiente de las clases de producto concretas.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    La interfaz «Product» declara las operaciones que todos los productos concretos
    deben implementar.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Los productos concretos proporcionan diversas implementaciones de la interfaz Product.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    El código del cliente funciona con una instancia de un creador concreto, aunque sea a través de
    su interfaz base. Siempre que el cliente siga trabajando con el creador a través de
    la interfaz base, se le puede pasar cualquier subclase de dicho creador.
    """

    print(f"Client: No sé qué clase es la del creador, pero funciona de todos modos.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Lanzado con ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Lanzado con ConcreteCreator2.")
    client_code(ConcreteCreator2())