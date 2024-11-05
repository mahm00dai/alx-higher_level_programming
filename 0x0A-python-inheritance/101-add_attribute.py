#!/usr/bin/python3
"""Module to add an attribute to an object if possible."""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute is to be added.
        attr_name: The name of the attribute to add.
        attr_value: The value of the attribute to add.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    # Check if we can set the attribute
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    # Set the new attribute
    setattr(obj, attr_name, attr_value)
