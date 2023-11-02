#!/usr/bin/python3
""" a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices.
    the Args:
        m_a (list of lists of int/float): Matrix to be multiplied.
        m_b (list of lists of int/float): Matrix to be multiplied.
    the Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        TypeError: If one element of list of lists is not int/float.
        TypeError: If row of m_a or m_b are not the same size.
        ValueError: If m_a or m_b is empty.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
         A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    Matix_1 = []
    for x in range(len(m_b[0])):
        my_row = []
        for y in range(len(m_b)):
            my_row.append(m_b[y][x])
        Matix_1.append(my_row)

    Matrix_2 = []
    for row in m_a:
        my_row = []
        for column in Matix_1:
            product = 0
            for m in range(len(Matix_1[0])):
                product += row[m] * column[m]
            my_row.append(product)
        Matrix_2.append(my_row)

    return Matrix_2
