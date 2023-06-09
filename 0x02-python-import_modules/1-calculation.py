#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as math
    a = 10
    b = 5
    print("{0:d} + {1:d} = {2:d}".format(a, b, math.add(a, b)))
    print("{0:d} - {1:d} = {2:d}".format(a, b, math.sub(a, b)))
    print("{0:d} * {1:d} = {2:d}".format(a, b, math.mul(a, b)))
    print("{0:d} / {1:d} = {2:d}".format(a, b, math.div(a, b)))
