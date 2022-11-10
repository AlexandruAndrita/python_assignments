def number_digits(value):
    count=0
    while value:
        count+=1
        value//=10
    return count


def round_(number, ndigits: int = None):
    fractional_part=number%1
    if ndigits==None:
        if fractional_part>=0.5:
            return int(number+1.0)
        elif fractional_part<0.5:
            return int(number-1.0)
    elif ndigits>=0:
        pass
    elif ndigits<0:
        number=int(number)
        digits=number_digits(number) #number of digits of the number
        ndigits*=(-1)
        number=str(number)
        pass



print("round_(777.777) = {}".format(round_(777.777)))
print("round_(777.777, 0) = {}".format(round_(777.777, 0)))
print("round_(777.777, 1) = {}".format(round_(777.777, 1)))
print("round_(777.777, 2) = {}".format(round_(777.777, 2)))
print("round_(777.777, 3) = {}".format(round_(777.777, 3)))
print("round_(777.777, 4) = {}".format(round_(777.777, 4)))
print("round_(777.777, -1) = {}".format(round_(777.777, -1)))
print("round_(777.777, -2) = {}".format(round_(777.777, -2)))
print("round_(777.777, -3) = {}".format(round_(777.777, -3)))

print(777.786%1)
print(777.786%0.1)
print(777.786%0.2)
print(777.786%0.3)
print(777.786%3)

import math

print(math.floor(23.34))
