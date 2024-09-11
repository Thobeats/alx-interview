#!/usr/bin/env python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix: list[list]):
    matrix[:] = [
        [matrix[len(matrix) - j - 1][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
        ]
    return
