#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix: list[list]):
    """Rotate 2D Matrix in 90 degrees"""
    matrix[:] = [
        [matrix[len(matrix) - j - 1][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
        ]
    return
