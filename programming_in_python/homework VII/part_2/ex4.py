from ex3 import Shape


class Rectangle(Shape):
    def __init__(self,x: int,y: int,width: int,height: int):
        super().__init__(x,y)
        self.width=width
        self.height=height

    def to_string(self) ->str:
        class_name = type(self).__name__
        string_representation="{}: x={}, y={}, width={}, height={}".format(class_name,self.x,self.y,self.width,self.height)
        return string_representation

    def area(self) -> float:
        return float(self.width*self.height)
