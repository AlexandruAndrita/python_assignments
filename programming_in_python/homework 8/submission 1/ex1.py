import math


class Complex:
    def __init__(self,real: float, imaginary: float):
        self.real=real
        self.imaginary=imaginary

    def __eq__(self, other):
        if isinstance(other,Complex):
            if self.real==other.real and self.imaginary==other.imaginary:
                return True
            return False
        return NotImplemented

    def __repr__(self):
        return f"Complex(real={self.real}, imaginary={self.imaginary})"

    def __str__(self):
        if self.imaginary>=0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {self.imaginary*(-1)}i"

    def __abs__(self):
        return math.sqrt(self.real**2+self.imaginary**2)

    def __add__(self, other):
        if isinstance(other,Complex):
            real_part=self.real+other.real
            imaginary_part=self.imaginary+other.imaginary
            return Complex(real_part,imaginary_part)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other,Complex):
            self.real=self.real+other.real
            self.imaginary=self.imaginary+other.imaginary
            return self
        return NotImplemented

    @staticmethod
    def add_all(comp: "Complex", *comps: "Complex") -> "Complex":
        if not isinstance(comp,Complex):
            raise TypeError("comp is not an instance of class 'Complex'")
        for class_object in comps:
            if not isinstance(class_object,Complex):
                raise TypeError("member of comps is not an instance of class 'Complex'")

        new_object=Complex(comp.real,comp.imaginary)
        for class_object in comps:
            new_object.real=new_object.real+class_object.real
            new_object.imaginary=new_object.imaginary+class_object.imaginary

        return new_object

