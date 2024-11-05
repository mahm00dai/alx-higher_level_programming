#!/usr/bin/python3
"""Module defining a rebellious integer class MyInt."""

class MyInt(int):
    """Class that inverts the equality and inequality operators."""
    
    def __eq__(self, other):
        """Invert the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the inequality operator."""
        return super().__eq__(other)
