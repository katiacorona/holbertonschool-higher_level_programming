#!/usr/bin/python3
from sys import argv

""" Prints the number of and the list of its arguments """
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} argument:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
