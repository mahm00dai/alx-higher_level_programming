#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a Square with a given size.

        Args:
            size (int or float): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private instance attribute

    def area(self):
        """Return the current area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """Return True if this square's area is less than the other's.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: Comparison result.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square's area is less tther's.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: Comparison result.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """Return True if this square's area is equal to the other's.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: Comparison result.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if this square's area is not equal to the other's.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: Comparison result.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Return True if this square's area is greater than the other's.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: Comparison result.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square's area is greateother's.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: Comparison result.
        """
        return self.area() >= other.area()
