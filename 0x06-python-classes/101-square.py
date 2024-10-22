#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with a given size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private instance attribute

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Private instance attribute

    def area(self):
        """Return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square in stdout using the character #."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print("")  # Print empty lines for vertical position
        for row in range(self.__size):
            print(" " * self.position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square for printing.

        Returns:
            str: The square printed with the character #.
        """
        output = []
        if self.__size == 0:
            return ""
        for i in range(self.position[1]):
            output.append("")  # Append empty lines for vertical position
        for row in range(self.__size):
            output.append(" " * self.position[0] + "#" * self.__size)
        return "\n".join(output)
