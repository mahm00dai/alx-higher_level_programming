#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
"""

class MyList(list):
    """
    MyList is a subclass of the built-in list class.
    It provides an additional method to print the list sorted.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
