#!/usr/bin/python3

""" Prints the number of and the list of its arguments """
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args == 0:
        print("{} arguments.".format(args))
    elif args == 1:
        print("{} argument:".format(args))
    else:
        print("{} arguments:".format(args))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
