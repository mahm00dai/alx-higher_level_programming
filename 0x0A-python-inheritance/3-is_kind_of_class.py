#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a specified class or
    if it is an instance of a class that inherited from it.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or an inherited class,
        otherwise False.
    """
    return isinstance(obj, a_class)
