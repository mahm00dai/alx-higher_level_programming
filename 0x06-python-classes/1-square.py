#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square with a private attribute size."""

    def __init__(self, size):
        """Initialize the square with the given size."""
        self.__size = size  # Private instance attribute
