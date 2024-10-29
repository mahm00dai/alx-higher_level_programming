#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        ndarray: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists,
                    or if the elements are not integers or floats.
    """

    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        # Re-raise NumPy's error which provides specific shape-related issues
        raise ValueError(e)
