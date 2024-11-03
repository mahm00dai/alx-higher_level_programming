#!/usr/bin/python3
class LockedClass:
    """A class that prevents the creation of new instance attributes
    except for 'first_name'."""

    __slots__ = ['first_name']

    def __init__(self):
        """Initialize a LockedClass instance without any attributes."""
        pass
