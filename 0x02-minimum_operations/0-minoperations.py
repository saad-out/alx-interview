#!/usr/bin/python3
"""
This module contains the minOperations function that calculates
the fewest number of operations needed to result in exactly n H
characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.
    Args:
        n (int): The target number of characters
    Returns:
        int: The fewest number of operations needed to result in
            exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    return 0
