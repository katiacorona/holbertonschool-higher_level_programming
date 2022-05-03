#!/usr/bin/python3

if __name__ == "__main__":
    """ Import a module and use every function printing results """
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
