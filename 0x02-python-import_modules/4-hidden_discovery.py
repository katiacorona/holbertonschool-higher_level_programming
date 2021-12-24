#!/usr/bin/python3

""" Prints the number of and the list of its arguments """
if __name__ == "__main__":
    import hidden_4

    lst = (dir(hidden_4))
    for name in lst:
        if name[:2] != '__':
            print(name)
