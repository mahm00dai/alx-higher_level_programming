#!/usr/bin/python3
def add_integer(a, b=98):
    """ Adds two integers. """
    if isinstance(a, float):
        if a == float('inf') or a == float('-inf'):
            raise TypeError("a must be an integer")
    if isinstance(b, float):
        if b == float('inf') or b == float('-inf'):
            raise TypeError("b must be an integer")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
