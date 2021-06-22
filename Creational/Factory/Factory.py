from __future__ import annotations
from abc import ABCMeta, abstractmethod

# Product interface.
class IProduct(metaclass=ABCMeta):
    """Product Interface"""

    def operation(self) -> str:
        """Operaton definition"""
        pass


class Creator(metaclass=ABCMeta):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        return f"Creator code worked with {product.operation()}"


class CreatorA(Creator):
    def factory_method(self) -> IProduct:
        return ProductA()


class CreatorB(Creator):
    def factory_method(self) -> IProduct:
        return ProductB()


class ProductA(IProduct):
    def operation(self) -> str:
        return f"Created by creatorA"


class ProductB(IProduct):
    def operation(self) -> str:
        return f"Created by creatorB"


def main(creator: Creator) -> None:
    print(f"called{creator.some_operation()}")


main(CreatorA())
