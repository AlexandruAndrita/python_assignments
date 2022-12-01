import math


class Complex:
    def __init__(self,real: float, imaginary: float):
        self.real=real
        self.imaginary=imaginary

    def print(self):
        if self.imaginary>=0:
            print(f"{self.real} + {self.imaginary}i")
        else:
            print(f"{self.real} - {self.imaginary*(-1)}i")

    def abs(self) -> float:
        return math.sqrt(self.real**2+self.imaginary**2)

    def add(self,other: "Complex"):
        if not isinstance(other,Complex):
            raise TypeError(f"other is of type {type(other)} instead of Complex")
        self.real+=other.real
        self.imaginary+=other.imaginary

    @staticmethod
    def add_all(comp: "Complex", *comps:"Complex") -> "Complex":
        if not isinstance(comp, Complex):
            raise TypeError(f"comp is of type {type(comp)} instead of Complex")
        for class_object in comps:
            if not isinstance(class_object,Complex):
                raise TypeError(f"comps is of type {type(class_object)} instead of Complex")

        new_object=Complex(0.0,0.0)
        new_object.real+=comp.real
        new_object.imaginary+=comp.imaginary
        for class_object in comps:
            new_object.real+=class_object.real
            new_object.imaginary+=class_object.imaginary
        return new_object

