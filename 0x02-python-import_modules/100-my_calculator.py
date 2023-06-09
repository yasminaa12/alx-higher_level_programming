#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    opt = [("+", add), ("-", sub), ("*", mul), ("/", div)]
    argc = len(argv)
    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if (argv[2] in "+-*/"):
        a = int(argv[1])
        b = int(argv[3])
        for sym, op in opt:
            if sym == argv[2]:
                func = op
                break
        res = func(a, b)
        print("{0:d} {2:s} {1:d} = {3:d}".format(a, b, argv[2], res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
