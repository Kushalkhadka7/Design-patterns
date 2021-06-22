from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class IGraphics(ABC):
    @abstractmethod
    def draw(self):
        pass

    def move(self):
        pass


class Dot(IGraphics):
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Dot Drawing on {self.x},{self.y}")

    def move(self):
        print(f"Moving from {self.x},{self.y} to {self.x + 2},{self.y + 2}")


class Circle(Dot):
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Circle Drawing on {self.x},{self.y}")


class CompoundGraphic(IGraphics):
    children: List[IGraphics] = []

    def add(self, child: IGraphics):
        self.children.append(child)

    def remove(self, child):
        self.children.pop(child)

    def draw(self):
        for c in self.children:
            c.draw()

    def move(self):
        for c in self.children:
            c.move()


class Application:
    c_g: IGraphics

    def __init__(self):
        self.c_g = CompoundGraphic()

    def load(self):
        self.c_g.add(Dot(1, 1))
        self.c_g.add(Circle(2, 2))

    def draw(self):
        self.c_g.draw()


print(Application().draw())
