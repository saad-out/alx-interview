#!/usr/bin/python3
"""
This module contains a function to solve to `Rotate 2D Matrix` problem
"""


def rotate_square(matrix, length, start_index, end_index):
    """
    Rotates a square of a 2D matrix 90 degrees clockwise

    Args:
        matrix (list): a 2D matrix
        length (int): the length of the square
        start_index (int): the starting index of the square
        end_index (int): the ending index of the square

    Returns:
        None
    """
    top = []
    bottom = []
    left = []
    right = []
    for i in range(start_index, length):
        top.append(matrix[start_index][i])
        bottom.append(matrix[end_index][i])
        left.append(matrix[i][start_index])
        right.append(matrix[i][end_index])

    j = 0
    k = -1
    for i in range(start_index, length):
        matrix[i][end_index] = top[j]
        matrix[i][start_index] = bottom[j]
        matrix[end_index][i] = right[k]
        matrix[start_index][i] = left[k]
        j += 1
        k -= 1


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise

    Args:
        matrix (list): a 2D matrix

    Returns:
        None
    """
    START_INDEX = 0
    END_INDEX = len(matrix) - 1
    LENGTH = len(matrix)
    for i in range(len(matrix) // 2):
        rotate_square(matrix, LENGTH, START_INDEX, END_INDEX)
        START_INDEX += 1
        END_INDEX -= 1
        LENGTH -= 1
