#!/usr/bin/python3

if __name__ == "__main__":
    # Importing the add function from add_0.py
    from add_0 import add

    # Assigning values to a and b
    a = 1
    b = 2

    # Printing the result in the specified format
    print("{} + {} = {}".format(a, b, add(a=1, b=2)))
