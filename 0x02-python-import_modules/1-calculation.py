#!/usr/bin/python3

""" Imports functions from calculaotr_1.py and prints the results
using each function """

if __name__ == "__main__":

    import calculator_1 as calc
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
