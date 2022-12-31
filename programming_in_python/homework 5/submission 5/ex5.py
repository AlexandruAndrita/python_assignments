def f(x: int):
    try:
        g(x)
        print("f1")
    except TypeError: #errorA
        print("f2")
        raise IndexError #errorC
    except ValueError: #errorB
        print("f3")
    else:
        print("f4")
    print("f5")

def g(x: int):
    try:
        h(x)
        print("g1")
    except TypeError: #errorA
        print("g2")
        if x < -10:
            raise IndexError #errorC
        print("g3")
    finally:
        print("g4")

def h(x: int):
    try:
        if x < 0:
            raise TypeError #errorA
        if x > 10:
            raise ValueError #errorB
    finally:
        print("h1")
        print("h2")

f(1)
print("\n")
f(-1)
print("\n")
f(15)
print("\n")
f(-15)
print("\n")