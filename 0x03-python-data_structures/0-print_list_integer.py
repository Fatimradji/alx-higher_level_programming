#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints integers of a list."""
    for f in range(len(my_list)):
        print("{:d}".format(my_list[f]))
