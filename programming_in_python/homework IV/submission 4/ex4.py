import math


def number_digits(value):
    count=0
    while value:
        count+=1
        value//=10
    return count


def round_(number, ndigits: int = None):
    fractional_part = number % 1

    if ndigits==None:
        if fractional_part>=0.5:
            return int(number+1.0)
        elif fractional_part<0.5:
            return int(number)

    elif ndigits>=0:
        number=math.ceil(number * math.pow(10, ndigits))
        number/=math.pow(10, ndigits)
        return number

    elif ndigits<0:
        tmp=int(number)
        number_copy=str(tmp)
        if ndigits*(-1)>len(number_copy):
            return 0.0
        else:
            number=math.ceil(number * math.pow(10, ndigits))
            number/=math.pow(10, ndigits)
            return number


print("round_(777.777) = {}".format(round_(777.777)))
print("round_(777.777, 0) = {}".format(round_(777.777, 0)))
print("round_(777.777, 1) = {}".format(round_(777.777, 1)))
print("round_(777.777, 2) = {}".format(round_(777.777, 2)))
print("round_(777.777, 3) = {}".format(round_(777.777, 3)))
print("round_(777.777, 4) = {}".format(round_(777.777, 4)))
print("round_(777.777, -1) = {}".format(round_(777.777, -1)))
print("round_(777.777, -2) = {}".format(round_(777.777, -2)))
print("round_(777.777, -3) = {}".format(round_(777.777, -3)))
print("round_(777.777, -4) = {}".format(round_(777.777, -4)))
