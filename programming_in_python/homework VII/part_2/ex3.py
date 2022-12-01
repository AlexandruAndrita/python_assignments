class Shape:
    def __init__(self,x: int,y: int):
        self.x=x
        self.y=y

    def to_string(self) -> str:
        class_name=type(self).__name__
        string_representation="{}: x={}, y={}".format(class_name,self.x,self.y)
        return string_representation

    def area(self) -> float:
        raise NotImplementedError

