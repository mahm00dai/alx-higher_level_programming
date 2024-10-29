#!/usr/bin/python3

def print_square(size):
    """Prints a square with the character #."""

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print('#' * size)
