def add_integer(a, b=98):
    """ Adds two integers or floats and returns the result as an integer.
    Args:
        a: First integer or float.
        b: Second integer or float, defaults to 98.
    Raises:
        TypeError: If a or b is not an integer or float.
    Returns:
        int: The sum of a and b, cast to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
