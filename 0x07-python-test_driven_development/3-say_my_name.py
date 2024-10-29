#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """ Prints My name is <first name> <last name> """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name
    print(f"My name is {first_name} {last_name}".strip() + " ")
