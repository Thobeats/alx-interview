#!/usr/bin/python3
"""Write a Pascal's Triangle Function"""


def pascal_triangle(n):
    """A function that creates a pacal triangle"""

    triangle = list()
    i = 1
    if n <= 0:
        return triangle
    while i <= n:
        if i == 1:
            triangle.append([1])
        if i == 2:
            triangle.append([1, 1])
        if i > 2:
            len_of_prev_result = len(triangle[i - 2])
            j = 0
            new_list = list()
            new_list.append(1)
            while j < len_of_prev_result - 1:
                new_list.append(triangle[i - 2][j] + triangle[i - 2][j + 1])
                j += 1
            new_list.append(1)
            triangle.append(new_list)
        i += 1
    return triangle
