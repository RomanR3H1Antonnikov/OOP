from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r


    def area(self):
        return math.pi * self.r ** 2


Rect1 = Rectangle(5, 4)
Circl1 = Circle(7)
print(Rectangle.area(Rect1))
print(Circle.area(Circl1))