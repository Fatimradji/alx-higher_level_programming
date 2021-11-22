#!/usr/bin/python3
def element_at(my_list, i):
    """we retrieves  element from a list """
    if i < 0 or i > len(my_list) - 1:
        return None
    else:
        return my_list[i]
