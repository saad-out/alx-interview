#!/usr/bin/python3
"""
This module contains a function to solve the island perimeter algorithm problem
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

    Args:
        grid (2D list): contains the water and lands

    Returns:
        (int) perimeter of island if it exists
    """
    permiter = 0
    for i, y in enumerate(grid):
        if i == 0 or i == len(grid) - 1:
            continue
        for j, x in enumerate(y):
            if x == 1 and j != 0 and j != len(y) - 1:
                sides = 4
                if grid[i][j - 1] == 1:
                    sides -= 1
                if grid[i][j + 1] == 1:
                    sides -= 1
                if grid[i - 1][j] == 1:
                    sides -= 1
                if grid[i + 1][j] == 1:
                    sides -= 1
                permiter += sides

    return permiter
