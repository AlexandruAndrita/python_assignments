"""
I computed the square root by rising the certain number to the power of 1/2.
I have also tried to implement it by myself with the binary search, with a precision of 10^(-5).
But I am not sure if that precision is enough or I should have used an even smaller number like 10^(-8).
"""


# def square_root(x):
#     right, left, middle = x,0,-1
#     while left<=right:
#         middle = (right + left)/2
#         if abs(middle**2-x)<=0.000001:
#             return middle
#         if middle**2<=x:
#             left=middle
#         else:
#             right=middle
#     return -1


def square_root(x):
    return x**(1/2)


a = float(input("Edge length: "))
print(f"Surface: {a**2*square_root(3):.4f}")
print(f"Volume: {a**3/12*square_root(2):.4f}")
print(f"Height: {a/3*square_root(6):.4f}")
