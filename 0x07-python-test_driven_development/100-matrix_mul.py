def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists,
                    if the elements are not integers or floats,
                    if the rows are not the same size.
        ValueError: If m_a or m_b is empty or if they cannot be multiplied.
    """
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            dot_product = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            result_row.append(dot_product)
        result.append(result_row)

    return result
