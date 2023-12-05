#!/usr/bin/python3


def max_integer(my_list=[]):
    """we areFinding biggest int of list."""
    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for u in range(len(my_list)):
        if my_list[u] > biggest:
            biggest = my_list[u]

    return (biggest)
