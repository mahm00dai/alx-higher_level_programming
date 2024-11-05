#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)  # Validate size
        self.__size = size  # Private attribute for size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
