from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def build_part_A(self) -> None:
        pass

    @abstractmethod
    def build_part_B(self) -> None:
        pass

    @abstractmethod
    def build_part_C(self) -> None:
        pass


class Product:
    def __init__(self) -> None:
        self.parts = []

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class BuilderA(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    def build_part_a(self) -> None:
        self._product.add("PartA1")

    def build_part_b(self) -> None:
        self._product.add("PartB1")

    def build_part_c(self) -> None:
        self._product.add("PartC1")

    @property
    def build_product(self) -> Product1:
        product = self._product
        self.reset()
        return product


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_product(self) -> None:
        self._builder.build_part_A()
        self._builder.build_part_B()
        self._builder.build_part_C()


def main():
    director = Director()
    builder = BuilderA()
    director.builder = builder

if __name__="__main__":
    main()
