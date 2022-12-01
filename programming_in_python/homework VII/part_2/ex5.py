from ex3 import Shape
import math


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius=radius

    def to_string(self) -> str:
        class_name = type(self).__name__
        string_representation="{}: x={}, y={}, radius={}".format(class_name,self.x,self.y,self.radius)
        return string_representation

    def area(self) -> float:
        return float(self.radius**2*math.pi)


