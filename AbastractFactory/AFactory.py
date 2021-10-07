from __future__ import annotations
from abc import ABCMeta, abstractmethod

class ProductA(metaclass=ABCMeta):
    @abstractmethod
    def useful_function_a(self)->str:
        pass


class ProductB(metaclass=ABCMeta):
    @abstractmethod
    def useful_function_b(self)->str:
        pass

class MainFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_product_a(self)->ProductA:
        pass

      @abstractmethod
    def create_product_b(self)->ProductB:
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class FactoryA(MainFactory):
    def create_product_a(self) -> ProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> ProductB:
        return ConcreteProductB1()

class FactoryB(MainFactory):
    def create_product_a(self) -> ProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> ProductB:
        return ConcreteProductB2()