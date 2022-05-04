#!/usr/bin/python3

""" Prints the number of and the list of the imported module's arguments """
if __name__ == "__main__":
    import hidden_4
    ls = dir(hidden_4)
    for name in ls:
        if name[:2] != '__':
            print(name)
